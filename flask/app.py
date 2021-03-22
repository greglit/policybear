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
import json



from beartools.data import icos
from beartools.cli import computations as cmp
from beartools.metadata import collect

#%%


def compare(co2eq,compareTo):
    areafrac_arctic = 3700000/510000000
    mass_global = 5.13*10**15
    mass_arctic = mass_global*areafrac_arctic
    tons = round((co2eq*1e-06*mass_arctic),3) # gt 1e-9
    return round(tons/comps[compareTo],1)

# complement time dims if not existent
def complement(df):
    for i in ['month','day','hour','minute','second']:
        if i not in list(df.columns):
            df[i] = 1
    return df

# load .csv into pd.Dataframe
def load_df(file):
    df = pd.read_csv(file+'.csv', sep=';')
    df = complement(df)
    df['time'] = [dt.datetime(Y,M,D,h,m,s)
                  for Y,M,D,h,m,s in zip(
                      df['year'],df['month'],df['day'],
                      df['hour'],df['minute'],df['second'])]
    df = df[['time','value']].set_index('time')
    return df

#%%

data_path = Path() / 'data/'

with open(data_path / 'paramsInfo.json') as f:
    paramsInfo = json.load(f)

metadata = pd.read_csv('metadata.csv',sep=';').set_index('index')
data_vars = list(metadata.index)            # ['co2','ch4']

# load files into dict
data = {i: load_df(i) for i in data_vars}


#%%

params = {
    'ch4': 'ICOS ATC NRT CH4 growing time series',
    'co2': 'ICOS ATC NRT CO2 growing time series'
}

data = {}


def dct_size(dct):
    size = np.sum([sys.getsizeof(v)/1024**2 for v in dct.values()])
    print('Size of Dictionary below {} MB'.format(math.ceil(size)))

dct_size(data)

#%%

# get time.minmax vals for metadata dict
# data_range = pd.DataFrame(
#     {i: {'minDate':data[i].index.min().strftime('%Y-%m-%d'),
#          'maxDate':data[i].index.max().strftime('%Y-%m-%d'),
#          'minYear':data[i].index.min().strftime('%Y'),
#          'maxYear':data[i].index.max().strftime('%Y')} for i in data_vars}).T
# metadata[['minDate','maxDate','minYear','maxYear']] = data_range
# metadata['compareTo'] = [['cows','cars'],['cows','cars']]
# metadata = metadata.to_dict('index')

unit_conversion = {'ch4': 0.001,
                   'co2': 1}

comps = {'cows': 100*0.001*23,
         'cars': 110*1e-6*12000}

# def return_period(df, start_date,end_date):
#     begin,end = pd.Timestamp(start_date),pd.Timestamp(str(int(end_date)+1))
#     mask = (df.index >= begin) & (df.index <= end)
#     return df.loc[mask]

def return_change(df):
    # dmin,dmax = df['value'].loc[df.index.min()],df['value'].loc[df.index.max()]
    ymeans = [round(df.loc[df.index.year == y]['value'].mean(), 2) for y in np.unique(df.index.year)]
    delta = ymeans[-1]-ymeans[0]
    return round(delta,2), round(ymeans[0],2), round(ymeans[-1],2)



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

# one route should ask for the data of one station
# another route calculates from df.data for different years
# if another station is selected the first route asks again for a new data
# if so it get added to the existing df.data
# delete df after inactivity

#%%



#%%
# param = 'ch4'
# for i in ['HEL','ZEP','CMN','RUN','LMP','OPE','PAL','PUY','SAC']:
#     t = icos.fetch(i,param, params[param])
#     t.collectData(data)
#
#
#     size = math.ceil(np.sum([sys.getsizeof(v)/1024**2 for v in data.values()]))
#
#     print(param,i)
#     if size > 1 :
#         raise MemoryError('size reached limit of {} MB'.format(size-1))

#da = TEST['HEL']

# da = cmp.Period(data['HEL'][['ch4']])
# da_change = cmp.Comp(da.period(2020,2021)).change('M')


#%%

@app.route('/datapoints/')
def datapoints():
    obsStation  =  request.args.get('station')
    param       = request.args.get('param')
    start       = request.args.get('startdate') # which format ???
    end         =  request.args.get('enddate') # which format ???

    # ICOS = icos.fetch('ZEP', 'ch4', 'ICOS ATC NRT CH4 growing...')
    ICOS = icos.fetch(obsStation, param, params[param]) # rename params
    ICOS.collectData(data)    # empty dictionary called data

    da = cmp.Period(data[obsStation][[param]])
    C = cmp.Comp(da.period(start,end))
    C.change()

    #####################################################
    # data_key = request.args.get('dataset')
    # df = data[data_key]
    # start_date = request.args.get('startdate')
    # end_date = request.args.get('enddate')
    # period = return_period(df,start_date,end_date)
    # change,ymin,ymax = return_change(period)
    # # return render_template('index.html')
    # x = round(change * unit_conversion[data_key],4)
    # co2eq = x*23 if data_key=='ch4' else x
    # response = {'dataset': data_key,
    #             'begin_period': period.index.min().strftime("%Y"),
    #             'end_period': period.index.max().strftime("%Y"),
    #             'change': x,
    #             'begin_data': round(ymin * unit_conversion[data_key],2),
    #             'end_data': round(ymax * unit_conversion[data_key],2)}
    # compareTo = request.args.get('compareTo')
    # if compareTo:
    #     response['comp_amount'] = compare(co2eq, compareTo)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)


