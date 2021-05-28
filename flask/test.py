#!/usr/bin/python3
"""
Created Mar 12, 2021

Testing ...
"""
import os
import sys
import math
import pathlib
from pathlib import Path

import pandas as pd
import numpy as np
import datetime as dt
import dateutil
from dateutil import relativedelta
import json

#####################################################
# METHODS
from beartools.data import icos
from beartools.cli import computations as cmp
from beartools.cli.compare import CompareTo
from beartools.metadata.specs import ParamSpecs

# VARS
from beartools.metadata.specs import param_specs
from beartools.cli.compare import benchmarks

#%%

data_swap = {}
data_swapped_info = {}

#%%

param = 'co2'
obsStation = 'ZEP'  # KIT, NOR, ZEP
start = '2018'
end = '2020'

PS = ParamSpecs(param, param_specs)
#%%

ICOS = icos.Fetch(obsStation, PS, data_swap)
# writing data fetch into data swap dct
ICOS.fetch_and_swap_data(data_swap)


x = data_swap[obsStation][[param]]

P = cmp.Period(x, start, end)
da_period = P.select_period()
CMP = cmp.Compute(da_period, P.rule)
da_resamp = CMP.mean()
resamp_rule = 'monthly' if P.rule == 'M' else 'annual'

# change
start_abs_value = round(CMP.value_ref(), PS.decimals)
end_abs_value = round(CMP.value_comp(), PS.decimals)
change = round(CMP.change(), PS.decimals)
change_pct = round((CMP.change() / start_abs_value) * 100, 1)

period_begin = CMP.df.index.min()
period_end = CMP.df.index.max()
delta_period = relativedelta.relativedelta(period_end, period_begin)
t = '%{}Y-%{}m'.format(delta_period.years, delta_period.months)
t2 = '{} months'.format(12 * delta_period.years + delta_period.months)

#%%

from beartools.metadata import collect

data_path = Path() / 'data/'
with open(data_path / 'paramsInfo.json') as f:
    paramsInfo = json.load(f)

with open(data_path / 'stationsInfo.json') as f:
    stationsInfo = json.load(f)

metadata = pd.read_csv('data/metadata.csv', sep=';').set_index('index')

meta = {}
for param in ['co2', 'ch4']:
    C = collect.Collect(paramsInfo[param])
    meta[param] = {}

    meta[param].update({
        'param_name': metadata.loc[param, 'description']
    })

    # map viewer properties
    meta[param].update({
        'map_centroid_latlon': (50.0, 8.0)
    })

    # station specific infos
    meta[param].update({
        'stations': {
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

#%%

from flask import send_file

@app.route('/data_preview')
def data_preview():
    file = data_path / 'plot_preview/empty_img.png'
    return send_file(file, mimetype='image/png')

# def get_image():
#     if request.args.get('type') == '1':
#        filename = 'ok.gif'
#     else:
#        filename = 'error.gif'
#     return send_file(filename, mimetype='image/gif')

#%%
# @app.route('/datasets/')
# def datasets():
#     meta = {}
#     for param in data_vars:
#         C = collect.Collect(paramsInfo[param])
#         meta[param] = {
#             'name': metadata.loc[param, 'name'],
#             'description': metadata.loc[param, 'description'],
#             'convertTo': ['cows', 'cars'],
#             'stations': C.stations(),
#             'stations_name': {station: stationsInfo[station]['name']
#                               for station in C.stations()},
#             'stations_country': {station: stationsInfo[station]['country']
#                                  for station in C.stations()}
#         }
#         meta[param]['timeStart'] = {st: C.time(st)[0] for st in C.stations()}
#         meta[param]['timeEnd'] = {st: C.time(st)[1] for st in C.stations()}
#
#     return jsonify(meta)
