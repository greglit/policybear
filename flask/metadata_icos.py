#!/usr/bin/python3
"""
Created Mar 17, 2021

Get all ICOS observatory stations that offer data for target parameter.
"""
import os
import json
import icoscp   # load data from icos data portal
from icoscp.station import station
from icoscp.cpb.dobj import Dobj
import pathlib
from pathlib import Path

data_path = Path() / 'data/'

path = os.getcwd()

params = {
    'ch4': 'ICOS ATC NRT CH4 growing time series',
    'co2': 'ICOS ATC NRT CO2 growing time series'
}

stations = station.getIdList(project='all', sort='name')


def getStationsInfo(ID):
    obsTower = station.get(ID).info()
    infoVars = {'name','lat','lon','country','project','uri'}
    info = {key: obsTower[key] for key in obsTower.keys() & infoVars}
    info.update({'dataVars': list(station.get(ID).products()[0])})
    return info

stationsInfo = {ID: getStationsInfo(ID) for ID in stations.id}

# write Infos on ICOS station to file
with open(path+'/data/stationsInfo.json', "w") as outfile:
    json.dump(stationsInfo, outfile)

#%%

class container:
    def __init__(self, param, stationId=None):
        self.param = param
        self.pName = params[self.param]
        self.ID = stationId

    def listStations(self):
        """List all stations with data for target param (e.g. 'CH4').
        """
        return [ID for ID in stationsInfo
                if self.pName in stationsInfo[ID]['dataVars']]

    def listCoords(self):
        def getCoords(stations):
            return {ID: (stationsInfo[ID]['lat'], stationsInfo[ID]['lon'])
                    for ID in stations}

        if self.ID == None:
            return getCoords(self.listStations())

        # several station IDs are given
        if isinstance(self.ID, list):
            return getCoords(self.ID)

        # single station ID is given
        if isinstance(self.ID, str):
            return (stationsInfo[self.ID]['lat'], stationsInfo[self.ID]['lon'])

    def getData(self, ID):
        """Fetch height data for target station ID.
        """
        data = station.get(ID).data()
        return data[data.specLabel == self.pName]#.samplingheight

    def listHeights(self):
        def f(stations):
            """Get height for each ID in list and return dict.
            """
            dst = {}
            for ID in stations:
                try:
                    data = self.getData(ID)['samplingheight']
                    dst[ID] = list(data.astype(float))
                except:
                    dst[ID] = list()
            return dst

        # no station ID is given
        if self.ID == None:
            return f(self.listStations())

            # several station IDs are given
        if isinstance(self.ID, list):
            return f(self.ID)

        # single station ID is given
        if isinstance(self.ID, str):
            try:
                data = self.getData(self.ID)['samplingheight']
                return list(data.astype(float))
            except:
                return list()

    def listTime(self):
        def t(stations):
            dst = {}
            for ID in stations:
                data = self.getData(ID)[['timeStart','timeEnd']]
                dst[ID] = [(i,j) for i,j in zip(data['timeStart'],data['timeEnd'])]
            return dst

        if self.ID == None:
            return t(self.listStations())

        if isinstance(self.ID, list):
            return t(self.ID)

        if isinstance(self.ID, str):
            data = self.getData(ID)[['timeStart', 'timeEnd']]
            return [(i, j) for i, j in zip(data['timeStart'], data['timeEnd'])]

dst = {param: {
    'stations': container(param).listStations(),
    'period' : container(param).listTime(),
    #'coordinates': container(param).listCoords(),
    'height': container(param).listHeights()
} for param in params}

with open(path+'/data/paramsInfo.json', 'w') as outfile:
    json.dump(dst, outfile)




# # assign icos variable names
# towerVars = {'ch4': 'ICOS ATC NRT CH4 growing time series',
#              'co2': 'ICOS ATC NRT CO2 growing time series'}
#
# # get all ICOS stations that offer data for target param (e.g. CH4, CO2)
# def f(ID,param):
#     """Fetch metadata of ICOS observation station (ID),
#     select desired variables and return target parameter (e.g. CH4, CO2) as dict.
#
#     Parameters:
#     -----------
#     ID : str, station ID (e.g. 'ZEP')
#     param : str, parameter (e.g. 'CH4')
#
#     """
#     data = station.get(ID).data()
#     data = data[['dobj','timeStart','timeEnd','specLabel','samplingheight','bytes']]
#     return data[data.specLabel == param].to_dict('index')
#
# metadata = {}
# for param in towerVars:
#     metadata[param] = {
#         ID: f(ID,towerVars[param]) for ID in stations.id[:]
#         if towerVars[param] in list(station.get(ID).products()[0])
#     }
#
# # export metadata dictionary as json object
# with open("metadata_icos.json", "w") as outfile:
#     json.dump(metadata, outfile)



# END OF FILE

#%%

