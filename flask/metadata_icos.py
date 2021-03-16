#!/usr/bin/python3
"""
Created Mar 15, 2021

Get all ICOS observatory stations that offer data for target parameter.
"""
import json
import icoscp   # load data from icos data portal
from icoscp.station import station
from icoscp.cpb.dobj import Dobj

stations = station.getIdList(project='all', sort='name')

# assign icos variable names
towerVars = {'ch4': 'ICOS ATC NRT CH4 growing time series',
             'co2': 'ICOS ATC NRT CO2 growing time series'}

# get all ICOS stations that offer data for target param (e.g. CH4, CO2)
def f(ID,param):
    """Fetch metadata of ICOS observation station (ID),
    select desired variables and return target parameter (e.g. CH4, CO2) as dict.

    Parameters:
    -----------
    ID : str, station ID (e.g. 'ZEP')
    param : str, parameter (e.g. 'CH4')

    """
    data = station.get(ID).data()
    data = data[['dobj','timeStart','timeEnd','specLabel','samplingheight','bytes']]
    return data[data.specLabel == param].to_dict('index')

metadata = {}
for param in towerVars:
    metadata[param] = {
        ID: f(ID,towerVars[param]) for ID in stations.id[:]
        if towerVars[param] in list(station.get(ID).products()[0])
    }

# export metadata dictionary as json object
with open("metadata_icos.json", "w") as outfile:
    json.dump(metadata, outfile)



# END OF FILE
