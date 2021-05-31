#!/usr/bin/python3
"""
Created May 30, 2021

Database updates on MongoDB server.
"""

import os
import sys
import json
import pymongo
from pymongo import MongoClient

import pathlib
from pathlib import Path
import pandas as pd

from . import mongodb

from beartools.metadata.specs import ParamSpecs, param_specs
from beartools.data import icos
from beartools.metadata import collect

# just for local testing
try:
    import cfgMongoDB            # in main dir
    cfgMongoDB.mongodb_env()
except:
    pass


#%% ICOS
data_path = Path() / 'data/'

with open(data_path / 'paramsInfo.json') as f:
    paramsInfo = json.load(f)

with open(data_path / 'stationsInfo.json') as f:
    stationsInfo = json.load(f)

meta = {}
for param in ['co2', 'ch4']:
    PS = ParamSpecs(param, param_specs)
    C = collect.Collect(paramsInfo[param])
    meta[param] = C.stations()

meta = {st: list(meta.keys()) for stations in meta.values() for st in stations}  # revert key / values

# MongoDB client configuration
mongodb_uri = os.environ['MONGODB_URI']
client = MongoClient(mongodb_uri)

db_data = client['data']            # database
db_icos = db_data['icos']           # database collection

for station, params in meta.items():
    data = {}
    for param in params:
        PS = ParamSpecs(param, param_specs)
        ICOS = icos.Fetch(station, PS, data)
        ICOS.fetch_and_swap_data(data)

    test = {
        'objectID': f'ts_icos_{station}',
        'tags': ['icos', 'time_series', 'in-situ', 'gas'] + params,
        'station_attrs': {
            'station_ID': station,
            'station_name': stationsInfo[station]['name'],
            'station_country': stationsInfo[station]['country'],
            'station_latlon':
                (stationsInfo[station]['lat'], stationsInfo[station]['lon']),
            'station_time_period':
                (C.time(station)[0], C.time(station)[1]),
        },
        'data': data[station].to_json()
    }

    collection = mongodb.Collection(db_collection=db_icos, data_dct=test)
    collection.status_obj()
    collection.upload_data()
