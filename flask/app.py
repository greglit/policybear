#!/usr/bin/python3
"""
Created Mar 12, 2021

App main file
"""

from flask import Flask, request, jsonify, redirect, send_file
from flask_cors import CORS

import os
import sys
import math
import pathlib
from pathlib import Path

import json
import pandas as pd
import numpy as np
import datetime as dt
import dateutil
from dateutil.relativedelta import relativedelta
import json

import pymongo
from pymongo import MongoClient
#####################################################
# just for local testing:
try:
    import cfgMongoDB
    cfgMongoDB.mongodb_env()
except:
    pass

#####################################################
# METHODS
from beartools.data import icos
from beartools.data import swap
from beartools.cli import computations as cmp
from beartools.cli.compare import CompareTo
from beartools.metadata.specs import ParamSpecs
from beartools.metadata import collect

# VARS
from beartools.metadata.specs import param_specs
from beartools.cli.compare import benchmarks


#%%

data_path = Path() / 'data/'

with open(data_path / 'paramsInfo.json') as f:
    paramsInfo = json.load(f)

with open(data_path / 'stationsInfo.json') as f:
    stationsInfo = json.load(f)

metadata = pd.read_csv('data/metadata.csv', sep=';').set_index('index')
data_vars = list(metadata.index)            # ['co2','ch4']

# create empty dct to temporarily store data, in order to not fetch
# data when station and parameter already called earlier
# OBSOLET
data_swap = {}
data_swapped_info = {}

#%% MongoDB settings

# MongoDB access
mongodb_uri = os.environ['MONGODB_URI']
client = MongoClient(mongodb_uri)

# MongoDB data storage
db_data = client['data']            # database
db_icos = db_data['icos']           # database collection

# just temporarily defined function to fetch data from mongoDB
def mongodb_to_df(collection,station,param):
    objectID = f'ts_icos_{station}'
    filter = {'objectID': objectID}
    data_fromDB = collection.find_one(filter=filter)
    print('fetching data from MongoDB server')
    df = pd.read_json(data_fromDB['data'])
    return df[[param]]

#%%

app = Flask(__name__)
CORS(app)

@app.route('/datasets/')
def datasets():
    meta = {}
    for param in ['co2', 'ch4']:
        PS = ParamSpecs(param, param_specs)
        C = collect.Collect(paramsInfo[param])

        # initialize empty meta dct
        meta[param] = {}
        # basic parameter specifications
        meta[param].update({
            'param_specs': {
                'param_name': PS.name,
                'param_category': PS.category,
                'param_conversion': ['cars', 'cows'],
                'param_description': PS.descrp
            }
        })

        # map viewer properties
        meta[param].update({
            'map_opts': {
                'map_centroid_latlon': (50.0, 8.0),
                'map_zoom': 5.0
            }
        })

        # station specific infos
        meta[param].update({
            'param_stations': {
                station: {
                    'station_name': stationsInfo[station]['name'],
                    'station_country': stationsInfo[station]['country'],
                    'station_latlon':
                        (stationsInfo[station]['lat'], stationsInfo[station]['lon']),
                    'station_time_period':
                        (C.time(station)[0], C.time(station)[1])
                }
                for station in C.stations()
            }
        })
    return jsonify(meta)

# NOT YET IMPLEMENTED: DATA PREVIEW
# @app.route('/data_preview/')
# def data_preview():
#     file = data_path / 'plot_preview/empty_img.png'
#     return send_file(file, mimetype='image/png')

#%%

@app.route('/datapoints/')
def datapoints():
    obsStation  = request.args.get('station')
    param       = request.args.get('param')
    start       = request.args.get('startdate') # '2020-01' or '2020'
    end         = request.args.get('enddate') # '2020-01' or '2020'
    compare_to   = request.args.get('compareTo')

    print(param,obsStation,start,end,compare_to)
    #######################################################
    # obsolet due to mongoDB fetching
    PS = ParamSpecs(param,param_specs)
    #
    # ICOS = icos.Fetch(obsStation, PS, data_swap)
    # # writing data fetch into data swap dct
    # ICOS.fetch_and_swap_data(data_swap)
    #
    # x = data_swap[obsStation][[param]]
    #######################################################

    x = mongodb_to_df(db_icos, obsStation, param)

    P = cmp.Period(x, start, end)
    da_period = P.select_period()
    CMP = cmp.Compute(da_period, P.rule)
    da_resamp = CMP.mean()
    resamp_rule = 'monthly' if P.rule == 'M' else 'annual'

    # change
    start_abs_value = round(CMP.value_ref(), PS.decimals)
    end_abs_value = round(CMP.value_comp(), PS.decimals)
    change = round(CMP.change(), PS.decimals)
    change_pct = round((CMP.change()/start_abs_value)*100, 1)

    # NOT YET IMPLEMENTED
    # period_begin, period_end, period_delta = P.period_info()

    period_begin = CMP.df.index.min()
    period_end = CMP.df.index.max()
    delta_period = relativedelta(period_end, period_begin)
    t = '%{}Y-%{}m'.format(delta_period.years,delta_period.months)
    t2 = '{} months'.format(12* delta_period.years + delta_period.months)

    response = {
        'station': obsStation,
        'param': param,
        'begin_period': period_begin.strftime('%b, %Y'),
        'end_period': period_end.strftime('%b, %Y'),
        'period': ([delta_period.years,delta_period.months,delta_period.days],t,t2),
        'change': change,
        'change_pct': change_pct,
        'start_abs_value': start_abs_value,
        'end_abs_value': end_abs_value,
        'unit': 'ppm',
        'resamp_rule': resamp_rule
    }

    if compare_to:
        comp = CompareTo(PS, change, benchmarks, compare_to)
        response['compare_amount'] = comp.calc()

    # # return render_template('index.html')

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)


