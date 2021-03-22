#!/usr/bin/python3
"""
Created Mar 19, 2021

Select period and compute means
"""


import pandas as pd

class Period:
    def __init__(self, df):
        self.df = df
        self.time = self.df.index
        self.param = list(self.df.columns)

    def period(self, start, end=None):
        start = pd.Timestamp(str(start), freq='D')

        if end == None:
            end = start + pd.tseries.offsets.YearEnd()
        else:
            end = pd.Timestamp(str(end)) + pd.tseries.offsets.YearEnd()

        mask = (self.time >= start) & (self.time <= end)
        return self.df.loc[mask]

class Comp():
    def __init__(self, df, rule='M'):
        self.df = df
        self.rule = rule

    def mean(self):
        return self.df.resample(self.rule).mean()

    def change(self):
        return list((self.mean().iloc[-1]) - (self.mean().iloc[0]))