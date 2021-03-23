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
        return float(self.value_ref() - self.value_comp())










# END OF FILE