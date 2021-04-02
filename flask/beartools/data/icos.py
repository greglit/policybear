#!/usr/bin/python3
"""
Created Apr 2, 2021

Get ICOS data.
"""

import pathlib
from pathlib import Path

import pandas as pd
import numpy as np

import icoscp
from icoscp.station import station
from icoscp.cpb.dobj import Dobj

from ..metadata.specs import ParamSpecs

class Fetch:
    def __init__(self, ID, ParamSpecs):
        self.ID = ID
        self.PS = ParamSpecs
        self.param = self.PS.param
        self.dataset = self.PS.dataset    # ["ICOS ATC CH4 Release", "ICOS ATC NRT CH4 growing time series"]
        self.metadata = self.get_metadata()

    def get_metadata(self):
        """
        """
        def preprocessing(meta):
            # make sure samplingheight type is float (otherwise object)
            meta['samplingheight'] = meta['samplingheight'].astype(float, errors='ignore')
            return meta
        print('debug: fetching metadata')

        meta = station.get(self.ID).data()
        meta = meta.loc[meta.specLabel.isin(self.dataset)]
        meta = preprocessing(meta)
        return meta

    def list_heights(self):
        return list(np.unique(self.metadata['samplingheight']))

    def select_height(self):
        height = self.list_heights()[0]
        return self.metadata.loc[self.metadata['samplingheight'] == height]

    def fetch_data(self, dobj):
        data = Dobj(dobj).data
        data = data[['TIMESTAMP', self.param]]
        return data.set_index('TIMESTAMP')  # ??? [['ch4']]

    def unit_conv(self, ds):
        """input as pd.Series"""
        return ds * self.PS.unit_conv

    def get_data(self):
        meta = self.select_height()
        dobjs = list(meta['dobj'])
        data = pd.concat(
            [self.fetch_data(dobj) for dobj in dobjs],
            axis=0,
            # keys=['ATC','ATC NRT'] # hierarchical index
        ) # check overlapping with verify_integrity, will return exception!!
        data.loc[:,self.param] = self.unit_conv(data.loc[:,self.param])
        return data[[self.param]]

    def collect_data(self, dct):
        if (self.ID not in dct):
            print('Fetching data for: {} and {}'.format(self.ID,self.param))
            data = self.get_data()
            dct[self.ID] = data

        elif self.param not in dct[self.ID].columns:
            print('Station {} loaded, fetching data for different parameter: {}'.format(self.ID,self.param))
            data = self.get_data()
            dct[self.ID] = pd.concat([dct[self.ID], data], axis=1)

        else:
            print('Skip fetching data, already loaded for {} and {}'.format(self.ID,self.param))


# END OF FILE