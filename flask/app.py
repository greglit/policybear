from flask import Flask, request, jsonify, redirect
from flask_cors import CORS

import os
from pathlib import Path

import pandas as pd
import numpy as np
import datetime as dt
import json

data_path = Path() / 'data' /

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

with open(data_path / 'paramsInfo.json') as f:
    paramsInfo = json.load(f)

metadata = pd.read_csv('metadata.csv',sep=';').set_index('index')
data_vars = list(metadata.index)            # ['co2','ch4']

# load files into dict
data = {i: load_df(i) for i in data_vars}

# get time.minmax vals for metadata dict
data_range = pd.DataFrame(
    {i: {'minDate':data[i].index.min().strftime('%Y-%m-%d'),
         'maxDate':data[i].index.max().strftime('%Y-%m-%d'),
         'minYear':data[i].index.min().strftime('%Y'),
         'maxYear':data[i].index.max().strftime('%Y')} for i in data_vars}).T
metadata[['minDate','maxDate','minYear','maxYear']] = data_range
metadata['compareTo'] = [['cows','cars'],['cows','cars']]
metadata = metadata.to_dict('index')

unit_conversion = {'ch4': 0.001,
                   'co2': 1}

comps = {'cows': 100*0.001*23,
         'cars': 110*1e-6*12000}

def return_period(df, start_date,end_date):
    begin,end = pd.Timestamp(start_date),pd.Timestamp(str(int(end_date)+1))
    mask = (df.index >= begin) & (df.index <= end)
    return df.loc[mask]

def return_change(df):
    # dmin,dmax = df['value'].loc[df.index.min()],df['value'].loc[df.index.max()]
    ymeans = [round(df.loc[df.index.year == y]['value'].mean(), 2) for y in np.unique(df.index.year)]
    delta = ymeans[-1]-ymeans[0]
    return round(delta,2), round(ymeans[0],2), round(ymeans[-1],2)

app = Flask(__name__)
CORS(app)

@app.route('/datasets/')
def datasets():
    return jsonify(metadata)

@app.route('/datapoints/')
def datapoints():
    data_key = request.args.get('dataset')
    df = data[data_key]
    start_date = request.args.get('startdate')
    end_date = request.args.get('enddate')
    period = return_period(df,start_date,end_date)
    change,ymin,ymax = return_change(period)
    stations = paramsInfo[data_key]['stations']
    # return render_template('index.html')
    x = round(change * unit_conversion[data_key],4)
    co2eq = x*23 if data_key=='ch4' else x
    response = {'dataset': data_key,
                'begin_period': period.index.min().strftime("%Y"),
                'end_period': period.index.max().strftime("%Y"),
                'change': x,
                'begin_data': round(ymin * unit_conversion[data_key],2),
                'end_data': round(ymax * unit_conversion[data_key],2),
                'stations': stations}
    compareTo = request.args.get('compareTo')
    if compareTo:
        response['comp_amount'] = compare(co2eq, compareTo)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)


