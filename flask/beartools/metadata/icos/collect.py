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

# from ..metadata.specs import ParamSpecs
from beartools.metadata.specs import ParamSpecs

#%%
# data_path = Path() / 'data/'
#
# with open(data_path / 'param_specs.json', 'r') as file:
#     param_specs = json.load(file)
# params = {param: param_specs[param]['dataset'] for param in ['ch4','co2']}
#
# def getStationsInfo(ID):
#     obsTower = station.get(ID).info()
#     infoVars = {'name','lat','lon','country','project','uri'}
#     info = {key: obsTower[key] for key in obsTower.keys() & infoVars}
#     info.update({'dataVars': list(station.get(ID).products()[0])})
#     return info
#
# stations = station.getIdList(project='all', sort='name')
# stationsInfo = {ID: getStationsInfo(ID) for ID in stations.id}
# # write Infos on ICOS station to file
# with open(data_path / 'stationsInfo.json', 'w') as file:
#     json.dump(stationsInfo, file)

#%%
###################################################################
###################################################################
class Collect:
    def __init__(self, param, param_label, stationId=None):
        self.param = param
        self.ID = stationId

        if isinstance(param_label, list):
            self.plabel = param_label
        else:
            self.plabel = [param_label]

    def get_data(self):
        """
        """
        def preprocessing(data):
            # make sure samplingheight type is float (otherwise object)
            data['samplingheight'] = data['samplingheight'].astype(float, errors='ignore')
            return data

        data = station.get(self.ID).data()
        data = data.loc[data.specLabel.isin(self.plabel)]
        data = preprocessing(data)
        return data

    def list_heights(self):
        data = self.get_data()
        return list(np.unique(data['samplingheight']))

    def select_height(self):
        height = self.list_heights()[0]
        data = self.get_data()
        data = data.loc[data['samplingheight'] == height]
        return data

    def list_period(self):
        data = self.select_height()   # improve! now: get data and select height
        return (data['timeStart'].min(), data['timeEnd'].max())

######################################################################################
#
# with open(data_path / 'stationsInfo.json', 'r') as file:
#     stationsInfo = json.load(file)
#
# def list_stations(stationsInfo, param_label):
#     stations = [ID for ID in stationsInfo
#                 if len(set(stationsInfo[ID]['dataVars']) & set(param_label)) == 2]
#     return stations
#
# paramsInfo = {}
# for param,param_label in params.items():
#     stations = list_stations(stationsInfo,param_label)
#     tmp = {'stations': {}, 'period': {}, 'height': {}}
#     tmp['stations'] = stations
#     for ID in stations:
#         C = Collect(param,param_label,ID)
#         period = C.list_period()
#         heights = C.list_heights()
#         tmp['period'][ID] = period
#         tmp['height'][ID] = heights
#     paramsInfo[param] = tmp
#     print('{} at {} different stations available'.format(param,len(stations)))
#
# with open(data_path / 'paramsInfo.json', 'w') as file:
#     json.dump(paramsInfo, file)
#

    # def list_stations(self):
    #     """List all stations with data for target param (e.g. 'CH4').
    #     """
    #     return [ID for ID in stationsInfo
    #             if self.plabel in stationsInfo[ID]['dataVars']]
    #
    # def list_time(self):
    #     def t(stations):
    #         dst = {}
    #         for ID in stations:
    #             data = self.get_data(ID)[['timeStart','timeEnd']]
    #             dst[ID] = [(i,j) for i,j in zip(data['timeStart'],data['timeEnd'])]
    #         return dst
    #
    #     if self.ID == None:
    #         return t(self.list_stations())
    #
    #     if isinstance(self.ID, list):
    #         return t(self.ID)
    #
    #     if isinstance(self.ID, str):
    #         return t([self.ID])[self.ID]
    #         # data = self.get_data(self.ID)[['timeStart', 'timeEnd']]
    #         # return [(i, j) for i, j in zip(data['timeStart'], data['timeEnd'])]
    #
    # def listHeights(self):
    #     def f(stations):
    #         """Get height for each ID in list and return dict.
    #         """
    #         dst = {}
    #         for ID in stations:
    #             try:
    #                 data = self.get_data(ID)['samplingheight']
    #                 dst[ID] = list(data.astype(float))
    #             except:
    #                 dst[ID] = list()
    #         return dst
    #
    #     # no station ID is given
    #     if self.ID == None:
    #         return f(self.list_stations())
    #
    #         # several station IDs are given
    #     if isinstance(self.ID, list):
    #         return f(self.ID)
    #
    #     # single station ID is given
    #     if isinstance(self.ID, str):
    #         try:
    #             data = self.get_data(self.ID)['samplingheight']
    #             return list(data.astype(float))
    #         except:
    #             return list()
    #
    #
    #
    # def listCoords(self):
    #     def getCoords(stations):
    #         return {ID: (stationsInfo[ID]['lat'], stationsInfo[ID]['lon'])
    #                 for ID in stations}
    #
    #     if self.ID == None:
    #         return getCoords(self.list_stations())
    #
    #     # several station IDs are given
    #     if isinstance(self.ID, list):
    #         return getCoords(self.ID)
    #
    #     # single station ID is given
    #     if isinstance(self.ID, str):
    #         return (stationsInfo[self.ID]['lat'], stationsInfo[self.ID]['lon'])




# dst = {
#     param:
#         {
#         'stations': Container(param, param_label).list_stations(),
#         'period' : Container(param,param_label).list_time(),
#         # #'coordinates': Container(param).listCoords(),
#         'height': Container(param,param_label).listHeights()
#         } for param, param_label in params.items()
# }


#%%
#
#
# # class container to collect metadata
# class Collect:
#     def __init__(self, info_dct):
#         self.info = info_dct
#
#     def stations(self):
#         return self.info['stations']
#
#     def time(self, station):
#         def convertTime(date):
#             obj = dt.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
#             return [obj.year, obj.month]     # here you could put in a request
#
#         if station == None:
#             raise KeyError('Input attribute "station" not given. Please select a station!')
#         else:
#             start, end = self.info['period'][station][0]
#             start, end = convertTime(start), convertTime(end)
#             return (start, end)

#%%

