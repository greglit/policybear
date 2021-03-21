#!/usr/bin/python3
"""
Created Mar 19, 2021

Get ICOS data.
"""

import pathlib
from pathlib import Path

import pandas as pd
import numpy as np

import icoscp
from icoscp.station import station
from icoscp.cpb.dobj import Dobj


class fetch():
    def __init__(self, ID, param, paramLabel):
        self.ID = ID
        self.param = param
        self.paramLabel = paramLabel

    def getParamData(self):
        obs = station.get(self.ID).data()
        obs['samplingheight'][obs['samplingheight'] == ''] = np.nan
        condition = (
                            obs['specLabel'] == self.paramLabel) & (
                            obs['samplingheight'].astype(float) <= 500)
        obs = obs[condition]

        if obs.empty:
            raise ValueError('Dataframe is empty. No data for given condition available.')
        else:
            return obs.set_index(pd.Index(range(len(obs)))).to_dict()

    def getData(self):
        info = self.getParamData()
        data = Dobj(info['dobj'][0]).data
        data = data[['TIMESTAMP', self.param]]
        return data.set_index('TIMESTAMP')[[self.param]]

    def collectData(self, dct):
        if (self.ID not in dct):
            print('Station not available, fetching data ... ')
            data = self.getData()
            dct[self.ID] = data

        elif self.param not in dct[self.ID].columns:
            print('Parameter not available, fetching data ... ')
            data = self.getData()
            dct[self.ID] = pd.concat([dct[self.ID], data], axis=1)

        else:
            print('already downloaded')



#%%

