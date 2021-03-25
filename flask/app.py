from flask import Flask, request, jsonify, redirect
from flask_cors import CORS

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
from beartools.metadata import collect
from beartools.metadata.specs import ParamSpecs


# VARS
from beartools.metadata.specs import param_specs
from beartools.cli.compare import benchmarks



#%%

data_path = Path() / 'data/'

with open(data_path / 'paramsInfo.json') as f:
    paramsInfo = json.load(f)

metadata = pd.read_csv('metadata.csv',sep=';').set_index('index')
data_vars = list(metadata.index)            # ['co2','ch4']

data = {}


def dct_size(dct):
    size = np.sum([sys.getsizeof(v)/1024**2 for v in dct.values()])
    print('Size of Dictionary below {} MB ({})'.format(math.ceil(size), round(size,2)))

dct_size(data)
#%%

app = Flask(__name__)
CORS(app)

@app.route('/datasets/')
def datasets():
    meta = {}
    for param in data_vars:
        C = collect.Collect(paramsInfo[param])
        meta[param] = {'name': metadata.loc[param, 'name'],
                      'description': metadata.loc[param, 'description'],
                      'convertTo': ['cows', 'cars'],
                      'stations': C.stations()}
        meta[param]['timeStart'] = {st: C.time(st)[0] for st in C.stations()}
        meta[param]['timeEnd'] = {st: C.time(st)[1] for st in C.stations()}

    return jsonify(meta)


# empty
# param = 'ch4'
# obsStation = 'HEL'


#%%

@app.route('/datapoints/')
def datapoints():
    obsStation  = request.args.get('station')
    param       = request.args.get('param')
    start       = request.args.get('startdate') # which format ???
    end         = request.args.get('enddate') # which format ???
    compare_to   = request.args.get('compareTo')

    print(start,end)

    PS = ParamSpecs(param,param_specs)

    # ICOS = icos.fetch('ZEP', 'ch4', 'ICOS ATC NRT CH4 growing...')
    ICOS = icos.Fetch(obsStation, PS) # rename params
    ICOS.collectData(data)    # empty dictionary called data

    dct_size(data)

    x = data[obsStation][[param]]

    da = cmp.Period(x)
    C = cmp.Compute(da.period(start,end))

    # change
    change = round(C.change(), PS.decimals)
    start_abs_value = round(C.value_ref(), PS.decimals)
    end_abs_value = round(C.value_comp(), PS.decimals)

    period_begin = C.df.index.min()
    period_end = C.df.index.max()
    delta_period = relativedelta.relativedelta(period_end, period_begin)
    t = '%{}Y-%{}m'.format(delta_period.years,delta_period.months)
    t2 = '{} months'.format(12* delta_period.years + delta_period.months)

    response = {
        'station': obsStation,
        'param': param,
        'begin_period': period_begin.strftime('%b, %Y'),
        'end_period': period_end.strftime('%b, %Y'),
        'period': ([delta_period.years,delta_period.months,delta_period.days],t,t2),
        'change': change,
        'start_abs_value': start_abs_value,
        'end_abs_value': end_abs_value,
        'unit': 'ppm'
    }

    if compare_to:
        comp = CompareTo(PS, change, benchmarks, compare_to)
        response['compare_amount'] = comp.calc()

    # # return render_template('index.html')

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)


