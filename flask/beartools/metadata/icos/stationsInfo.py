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
#%%
data_path = Path() / 'data/'

def getStationsInfo(ID):
    obsTower = station.get(ID).info()
    infoVars = {'name','lat','lon','country','project','uri'}
    info = {key: obsTower[key] for key in obsTower.keys() & infoVars}
    info.update({'dataVars': list(station.get(ID).products()[0])})
    return info

stations = station.getIdList(project='all', sort='name')
stationsInfo = {ID: getStationsInfo(ID) for ID in stations.id}

# write Infos on ICOS station to file
with open(data_path / 'stationsInfo.json', 'w') as file:
    json.dump(stationsInfo, file)



# END OF FILE