#!/usr/bin/python3
"""
Created Mar 19, 2021

Select period and compute means
"""
import datetime as dt


# class container to collect metadata
class Collect:
    def __init__(self, info_dct):
        self.info = info_dct

    def stations(self):
        return self.info['stations']

    def time(self, station):
        def convertTime(date):
            obj = dt.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
            return [obj.year, obj.month]     # here you could put in a request

        if station == None:
            raise KeyError('Input attribute "station" not given. Please select a station!')
        else:
            start, end = self.info['period'][station][0]
            start, end = convertTime(start), convertTime(end)
            return (start, end)
