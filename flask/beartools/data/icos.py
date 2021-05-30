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

# swap inspection
from . import swap

# from ..metadata.specs import ParamSpecs

import logging
from logging.config import fileConfig

fileConfig('logging.cfg', disable_existing_loggers=False)

logger = logging.getLogger('dataLogger')

logger.debug('random logging message')

class Fetch:
    def __init__(self, ID, ParamSpecs, data_swap):
        self.ID = ID
        self.PS = ParamSpecs
        self.param = self.PS.param
        self.dataset = self.PS.dataset  # ["ICOS ATC CH4 Release", "ICOS ATC NRT CH4 growing time series"]
        self.data_swap = data_swap
        self.data_swap_status = self.check_data_swap_status()

        if not all(self.data_swap_status.values()):
            self.metadata = self.fetch_station_metadata()

    def header_data_swap(self):
        """
        return simple data swap header without the data.
        """
        header = {
            station: list(data.columns)
            for station, data in self.data_swap.items()
        }
        return header

    def check_data_swap_status(self):
        """
        Check if data already loaded into swap storage.
        """
        logger.debug(f'{self.__class__.__name__} : data swap status : '
                     f'... checking data availability in data swap storage ...')
        data_swapped = self.header_data_swap()

        if (self.ID not in data_swapped):
            station_status, param_status = False, False
        elif (self.param not in data_swapped[self.ID]):
            station_status, param_status = True, False
        else:
            station_status, param_status = True, True
        #logger.debug(f'{self.__main__.__name__} : data swap status : {self.ID}: {station_status},  {self.param}: {param_status}')
        return {'station': station_status, 'param': param_status}

    def fetch_station_metadata(self):
        logger.debug(f'{self.__class__.__name__} : station metadata : '
                     f'... fetching data infos, including dobj (download link) ...')

        def preprocessing(meta):
            # make sure samplingheight type is float (otherwise object)
            meta['samplingheight'] = meta['samplingheight'].astype(float, errors='ignore')
            return meta

        meta = station.get(self.ID).data()
        meta = meta.loc[meta.specLabel.isin(self.dataset)]
        meta = preprocessing(meta)
        logger.debug(f'{self.__class__.__name__} : station metadata : '
                     f'fetching metadata for {self.ID} successful.')
        return meta

    def list_heights(self):
        return list(np.unique(self.metadata['samplingheight']))

    def select_height(self):
        height = self.list_heights()[0]
        return self.metadata.loc[self.metadata['samplingheight'] == height]

    def get_data(self, dobj):
        data = Dobj(dobj).data
        data = data[['TIMESTAMP', self.param]]
        return data.set_index('TIMESTAMP')  # ??? [['ch4']]

    def unit_conv(self, ds):
        """input as pd.Series"""
        return ds * self.PS.unit_conv

    def fetch_data(self):
        logger.debug(f'{self.__class__.__name__} : data : ... fetching data ...')
        meta = self.select_height()
        dobjs = list(meta['dobj'])
        data = pd.concat(
            [self.get_data(dobj) for dobj in dobjs],
            axis=0,
            # keys=['ATC','ATC NRT'] # hierarchical index
        ) # check overlapping with verify_integrity, will return exception!!
        data.loc[:,self.param] = self.unit_conv(data.loc[:,self.param])
        return data[[self.param]]

    def fetch_and_swap_data(self, data_swap):
        if all(self.data_swap_status.values()):
            logger.debug(f'{self.__class__.__name__} : data : '
                         f'skip fetching, data already swapped.')

        elif not self.data_swap_status['station']:
            data = self.fetch_data()
            logger.debug(f'{self.__class__.__name__} : data : '
                         f'swaping data, creating entry:  {self.ID} with {self.param}')
            # self.data_swap[self.ID] = data
            data_swap[self.ID] = data

        elif not self.data_swap_status['param']:
            data = self.fetch_data()
            logger.debug(f'{self.__class__.__name__} : data : '
                         f'swaping data, creating entry:  ({self.ID}) with {self.param}')
            # self.data_swap[self.ID] = pd.concat([self.data_swap[self.ID], data], axis=1)
            data_swap[self.ID] = pd.concat([data_swap[self.ID], data], axis=1)

        # Check size of data swap if new data was fetched
        if not all(self.data_swap_status.values()):
            swap.inspect_data_swap(data_swap)


# END OF FILE