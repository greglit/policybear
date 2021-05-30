#!/usr/bin/python3
"""
Created May 30, 2021

Connect to MongoDB server.
"""

import os
import pymongo
from pymongo import MongoClient

#%%
# MongoDB access URI
mongodb_uri = os.environ.get('MONGODB_URI')
client = MongoClient(mongodb_uri)

db = client.admin
# Issue the serverStatus command and print the results
serverStatusResult = db.command("serverStatus")


# # creating new database "testing"
# db = client.testing
#
# sample_data = {
#     'stations': {
#         'name': 'KIT',
#         'latlon': [50.12,10.02]
#     },
#     'random': [2,4,6,7,8,9,9]
# }
#
# result = db.review
#
# def index():
#     times = os.environ.get('LSCOLORS')
#     return times
#
# index()


#%%

