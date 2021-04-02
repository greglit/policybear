#!/usr/bin/python3
"""
Created Mar 12, 2021

Testing ...
"""
import os
import sys
import math
import pathlib
from pathlib import Path

import pandas as pd
import numpy as np
import datetime as dt
import dateutil
from dateutil import relativedelta
import json

#####################################################
# METHODS
from beartools.data import icos
from beartools.cli import computations as cmp
from beartools.cli.compare import CompareTo
from beartools.metadata.specs import ParamSpecs

# VARS
from beartools.metadata.specs import param_specs
from beartools.cli.compare import benchmarks

#%%

data = {}

#%%

param = 'ch4'
obsStation = 'NOR'
start = '2018'
end = '2020'

PS = ParamSpecs(param, param_specs)
#%%

# ICOS = icos.fetch('ZEP', 'ch4', 'ICOS ATC NRT CH4 growing...')
ICOS = icos.Fetch(obsStation, PS)  # rename params
ICOS.collect_data(data)  # empty dictionary called data

# dct_size(data)

x = data[obsStation][[param]]

P = cmp.Period(x, start, end)
da_period = P.select_period()
CMP = cmp.Compute(da_period, P.rule)
da_resamp = CMP.mean()
resamp_rule = 'monthly' if P.rule == 'M' else 'annual'

# change
start_abs_value = round(CMP.value_ref(), PS.decimals)
end_abs_value = round(CMP.value_comp(), PS.decimals)
change = round(CMP.change(), PS.decimals)
change_pct = round((CMP.change() / start_abs_value) * 100, 1)

period_begin = CMP.df.index.min()
period_end = CMP.df.index.max()
delta_period = relativedelta.relativedelta(period_end, period_begin)
t = '%{}Y-%{}m'.format(delta_period.years, delta_period.months)
t2 = '{} months'.format(12 * delta_period.years + delta_period.months)


# END OF FILE