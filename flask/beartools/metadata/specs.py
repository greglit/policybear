#!/usr/bin/python3
"""
Created Mar 23, 2021

Parameter specifications
"""

import json
import pathlib
from pathlib import Path

data_path = Path() / 'data/'

with open(data_path / 'param_specs.json', 'r') as file:
    param_specs = json.load(file)

class ParamSpecs:
    def __init__(self,param, param_specs):
        self.param = param
        self.specs = param_specs

        self.name = self.specs[self.param]['long_name']
        self.descrp = self.specs[self.param]['description']
        self.dataset = self.specs[self.param]['dataset']
        self.label = self.specs[self.param]['label']
        self.variable = self.specs[self.param]['variable']
        self.access = self.specs[self.param]['access_folders']
        self.type = self.specs[self.param]['type']
        self.unit = self.specs[self.param]['unit']
        self.unit_conv = self.specs[self.param]['unit_conv']
        self.category = self.specs[self.param]['category']
        self.decimals = self.specs[self.param]['round_decimals']
        self.co2eq = self.specs[self.param]['co2eq_factor']


