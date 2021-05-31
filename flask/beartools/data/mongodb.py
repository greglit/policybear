#!/usr/bin/python3
"""
Created May 30, 2021

MongoDB server database administration.
"""

import os
import sys
import pymongo
from pymongo import MongoClient

class Collection:
    def __init__(self, db_collection, data_dct):
        self.collection = db_collection
        self.data_dct = data_dct
        self.objectID = self.data_dct['objectID']

    # def status_collection(self):
    #     if self.collection in self.db.list_collection_names():
    #         return True
    #     else:
    #         return False

    def status_obj(self):
        query = {'objectID': self.objectID}
        condition = self.collection.count_documents(query)
        if condition == 1: return True
        elif condition == 0: return False
        elif condition > 1: print('ERROR: there seem to be more '
                                  'than one entry with the same objectID')

    def upload_data(self):
        if self.status_obj():
            pass
            print('object already uploade')
            # self.db[self.collection].update_one(self.data)
        if not self.status_obj():
            self.add_data_obj()

    def add_data_obj(self):
        """
        Add data including all of its metadata (tags, station info, parameter info)
        """
        self.collection.insert_one(self.data_dct)
        print('uploaded data object to mongoDB database')

