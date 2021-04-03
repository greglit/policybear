#!/usr/bin/python3
"""
Created Mar 19, 2021

Select period and compute means
"""

import pandas as pd
# import xarray as xr
from dateutil.relativedelta import relativedelta

class Period:
    def __init__(self, df, start, end=None):
        self.df = df
        self.time = self.df.index
        self.param = list(self.df.columns)
        self.start = str(start)
        if end is None:
            self.end = end
        else:
            self.end = str(end)
        self.rule = self.resamp_rule()

    def resamp_rule(self):
        if (self.start.isdigit() & self.end.isdigit()):
            if self.start != self.end:
                rule = 'Y'
                print('annual values will be calculated ...')
            else: # just in case
                rule = 'M'
                print('monthly values will be calculated ...')
        else:
            rule = 'M'
            print('monthly values will be calculated ...')
        return rule

    def select_period(self):
        # if no end date given or start same as end, period is one year
        if (self.end is None) | (self.start == self.end):
            self.start = pd.Timestamp(self.start, freq='D')
            self.end = self.start + pd.tseries.offsets.YearEnd()
        else:
            self.start = pd.Timestamp(self.start, freq='D')
            self.end = pd.Timestamp(self.end, freq='D')
            if self.rule == 'Y':
                # only years are given, end of period is end of year
                self.end = self.end + pd.tseries.offsets.YearEnd()
            else:
                # years and months are given, end of period is end of month
                self.end = self.end + pd.tseries.offsets.MonthEnd()

        mask = (self.time >= self.start) & (self.time <= self.end)
        return self.df.loc[mask]

    def period_info(self):
        period = self.select_period()
        period_begin = period.index.min()
        period_end = period.index.max()
        period_delta = relativedelta(period_end,period_begin)
        if self.rule == 'Y':
            period_delta = period_delta + relativedelta(months=+1)
            format = '%Y'
        else:
            format = '%Y-%m'

        period_begin = period_begin.strftime(format)
        period_end = period_end.strftime(format)
        period_delta = '%{}Y-%{}m'.format(period_delta.years, period_delta.months)
        return (period_begin,period_end,period_delta)

class Compute:
    def __init__(self, df, rule='M'):
        self.df = df
        self.rule = rule

    # rename in rs_mean or resamp_mean()
    def mean(self):
        return self.df.resample(self.rule).mean()

    def value_ref(self):
        """begin of period"""
        return float(self.mean().iloc[0])

    def value_comp(self):
        """end of period"""
        return float(self.mean().iloc[-1])

    def change(self):
        """change compared to reference date (begin of period)"""
        return float(self.value_comp() - self.value_ref())


# NOT YET IMPLEMENTED
# ############################
# class GriddedData:
#     def __init(self, ds):
#         self.ds = ds
#         self.lat, self.lon = self.ds.lat, self.ds.lon
#
#     def comp_grid_cell_area(self):
#         try:
#             self.lon.dims
#         except:
#             self.lat = xr.DataArray(self.lat, dims='lat', name='lat')
#             self.lon = xr.DataArray(self.lon, dims='lon', name='lon')
#             self.lat = self.lat.assign_coords({'lat': self.lat}),
#             self.lon = self.lon.assign_coords({'lon': self.lon})
#
#         radius = 6.37122e6 # in meters
#
#         nlat, nlon = len(self.lat), len(self.lon)
#
#         lat_bounds = xr.DataArray(np.zeros((nlat+1)), dims=self.lat.dims[0], name=self.lat.name)
#         lat_bounds[0] = max(-90, self.lat[0]-0.5*np.abs(self.lat[1]-self.lat[0]))
#         lat_bounds[nlat] = min(90, self.lat[nlat-1]+0.5*np.abs(self.lat[nlat-2]-self.lat[nlat-1]))
#         lat_bounds[1:nlat] = 0.5*(self.lat[0:nlat-1].values + self.lat[1:nlat].values)
#         dlat = lat_bounds.diff(self.lat.name)
#
#         lon_bounds = xr.DataArray(np.zeros((nlon+1)), dims=self.lon.dims[0], name=self.lon.name)
#         lon_bounds[0] = self.lon[0]-0.5*np.abs(self.lon[1]-self.lon[0])
#         lon_bounds[nlon] = self.lon[nlon-1]+0.5*np.abs(self.lon[nlon-2]-self.lon[nlon-1])
#         lon_bounds[1:nlon] = 0.5*(self.lon[0:nlon-1].values + self.lon[1:nlon].values)
#         dlon = lon_bounds.diff(self.lon.name)
#
#         dlon_2d, dlat_2d = xr.broadcast(dlon,dlat)
#         lon_2d, lat_2d = xr.broadcast(self.lon,self.lat)
#
#         dy = radius * (dlat_2d * (np.pi/180.0))
#         dx = radius * np.multiply(dlon_2d * (np.pi/180.0),np.cos(lat_2d * (np.pi/180.0)))
#
#         area = np.abs(np.multiply(dx,dy))
#         return area
#
    # def area(self):
    #     area = self.comp_grid_cell_area()
    #     self.ds['cell_grid_area'] = area
    #     return self.ds
    #     #return #area.sum() * 1e-10
    #
    # def change(self):
    #     area = self.comp_grid_cell_area()
    #     self.ds['cell_grid_area'] = area
    #     begin = self.ds['sea_ice_cover'].isel(time=0) # here param label
    #     end = self.ds['sea_ice_cover'].isel(time=-1) # here param label
    #     change = (end-begin) * area
    #     return change.sum()


# END OF FILE