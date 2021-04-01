#!/usr/bin/python3
"""
Created Mar 28, 2021

Get NCEI data from https://www.ncei.noaa.gov/data/.
"""

import pathlib
from pathlib import Path

import requests
import pandas as pd
import xarray as xr

class Fetch():
    def __init__(self, start, end, ParamSpecs):
        self.start = start
        self.end = end
        self.PS = ParamSpecs    # container
        self.param = self.PS.param
        self.dataset = self.PS.dataset
        self.url_main = 'https://www.ncei.noaa.gov/data/'

    def build_url(self,timestamp):
        year = str(timestamp.year)
        month = str(timestamp.month).zfill(2)
        file = self.PS.label+'_{}{}.nc'.format(year,month)
        access = '/{}{}/{}/{}'.format(self.PS.access, year, month, file)
        url = self.url_main + self.PS.dataset + access
        print(url)
        return url

    def getData(self):
        urls = [self.build_url(pd.Timestamp(date_string)) for date_string in [self.start,self.end]]
        reqs = [requests.get(url) for url in urls]
        dst = [xr.open_dataset(req.content)[self.PS.variable] for req in reqs]
        dst = xr.concat(dst, dim='time')
        return dst.to_dataset()



    # def unit_conv(self):
    #     pass