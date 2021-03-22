#!/usr/bin/python3
"""
Created Mar 19, 2021

Get all ICOS data.
"""

import pathlib
from pathlib import Path

import pandas as pd
import numpy as np

import icoscp
from icoscp.station import station

#%%

stations = station.getIdList(project='all', sort='name')

def getParamData(ID):
    obs = station.get(ID).data()
    condition = (
                        obs['specLabel'] == 'ICOS ATC NRT CH4 growing time series') & (
                        obs['samplingheight'].astype(float) == 125)
    obs = obs[condition]
    return obs.set_index(pd.Index(range(len(obs)))).to_dict()


def getData(dobj):
    info = getParamData('KRE')
    data = Dobj(info['dobj'][0]).data
    data = data[['TIMESTAMP', 'ch4']].rename({'TIMESTAMP': 'time', 'ch4': 'value'})
    return data.set_index('TIMESTAMP')[['ch4']]

#%%

