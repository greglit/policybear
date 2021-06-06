#!/usr/bin/python3
"""
Created May 30, 2021

Connect to MongoDB server.
"""

import os
import sys
import pymongo
from pymongo import MongoClient

# from pprint import pprint

#%%
# just for local testing:
try:
    import cfgMongoDB
    cfgMongoDB.mongodb_env()
except:
    pass

#%%
# MongoDB access URI
mongodb_uri = os.environ['MONGODB_URI']
client = MongoClient(mongodb_uri)

# # Issue the serverStatus command and print the results
# db = client.admin
# serverStatusResult = db.command("serverStatus")

#%%

test = {
    'objectID': 'ts_icos_ZEP',
    'tags': ['time_series', 'ch4', 'co2', 'in-situ', 'gas'],
    'station_attrs': {
        'station_id': 'ZEP',
        'station_name': 'Zeppelin',
        'station_country': 'IT',
        'station_latlon': (50.123,10.1234),
        'station_url': '....',
        'station_description': ''
    },
    'data': {
        'ch4': 'asdf',
        'co2': [2,3,5,8,8,9]
    },
    'data_attrs': {
        'ch4': {
            'long_name': 'Methane (CH4) Concentration',
            'unit': 'ppm'
        },
        'co2': {
            'long_name': 'Carbon Dioxide (CO2) Concentration',
            'unit': 'ppm'
        }
    }
}

import pandas as pd
from beartools.data.mongodb import Collection

db_data = client['data']            # database
# db_icos = db_data['icos']           # database collection
db_test = db_data['test']


# query = {'objectID': 'Test'}
# filter = {'data': 1}
# found = db_icos.find(query, filter)
# for x in found:
#     print(pd.read_json(x['data']))



# query = {'objectID': 'ts_icos_ZEP'}
# filter = {'data': 1}

# data = list(db_icos.find(query, filter))#.limit(2))

df = pd.DataFrame(
    data={'ch4': [1,2,3,4,5,6,7,8,9], 'co2': [9,8,7,6,5,4,3,2,1]},
    index=range(9)
)

#%%


# # upload dataframe into mongoDB
# df.reset_index(inplace=True)
# data = df.to_dict('records')
# db_test.insert_one({'index': 'asdf', 'data': data})


db_data = client['data']            # database
db_icos = db_data['icos']           # database collection

objectID = "ts_icos_GAT"

# load data from MongoDB into dataframe
filter = {'objectID': objectID}
data_fromDB = db_icos.find_one(filter=filter)
df = pd.read_json(data_fromDB['data'])
# df.set_index('index', inplace=True)
print(df)

def mongodb_to_df(collection,station,param):
    objectID = f'ts_icos_{station}'
    filter = {'objectID': objectID}
    data_fromDB = collection.find_one(filter=filter)
    df = pd.read_json(data_fromDB['data'])
    return df[[param]]

df = mongodb_to_df(db_icos,'GAT','ch4')

df_update = pd.DataFrame(
    data={'ch4': [20,10,10,20], 'co2': [12,45,34,12]},
    index=range(9,13)
)
