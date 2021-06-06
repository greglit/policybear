#!/usr/bin/python3
"""
Created Apr 2, 2021


"""
import json
import icoscp
from icoscp.station import station
import pathlib
from pathlib import Path
import numpy as np

# from .collect import Collect
from beartools.metadata.icos.collect import Collect

#%%
data_path = Path() / 'data/'

with open(data_path / 'param_specs.json', 'r') as file:
    param_specs = json.load(file)
params = {param: param_specs[param]['dataset'] for param in ['ch4','co2']}

with open(data_path / 'stationsInfo.json', 'r') as file:
    stationsInfo = json.load(file)

def list_stations(stationsInfo, param_label):
    stations = [ID for ID in stationsInfo
                if len(set(stationsInfo[ID]['dataVars']) & set(param_label)) == 2]
    return stations

paramsInfo = {}
for param,param_label in params.items():
    stations = list_stations(stationsInfo,param_label)
    tmp = {'stations': {}, 'period': {}, 'height': {}}
    tmp['stations'] = stations
    for ID in stations:
        C = Collect(param,param_label,ID)
        period = C.list_period()
        heights = C.list_heights()
        tmp['period'][ID] = period
        tmp['height'][ID] = heights
    paramsInfo[param] = tmp
    print('{} at {} different stations available'.format(param,len(stations)))

with open(data_path / 'paramsInfo.json', 'w') as file:
    json.dump(paramsInfo, file)



# END OF FILE