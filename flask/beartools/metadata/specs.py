#!/usr/bin/python3
"""
Created Mar 23, 2021

Parameter specifications
"""

param_specs = {
    'ch4': {'dataset': 'ICOS ATC NRT CH4 growing time series',
            'column_label': 'ch4',
            'type': 'CH4 mixing ratio (dry mole fraction, ppb)',
            'unit': 'nmol mol-1',
            'unit_conv': 0.001,
            'category': 'gas',
            'co2eq_factor': 23,
            'round_decimals': 2},

    'co2': {'dataset': 'ICOS ATC NRT CO2 growing time series',
            'column_label': 'co2',
            'type': 'CO2 mixing ratio (dry mole fraction, ppm)',
            'unit': 'µmol mol-1',
            'unit_conv': 1,
            'category': 'gas',
            'co2eq_factor': 1,
            'round_decimals': 2}
}

class ParamSpecs:
    def __init__(self,param, param_specs):
        self.param = param
        self.specs = param_specs

        self.dataset = self.specs[self.param]['dataset']
        self.label = self.specs[self.param]['column_label']
        self.type = self.specs[self.param]['type']
        self.unit = self.specs[self.param]['unit']
        self.unit_conv = self.specs[self.param]['unit_conv']
        self.category = self.specs[self.param]['category']
        self.decimals = self.specs[self.param]['round_decimals']
        self.co2eq = self.specs[self.param]['co2eq_factor']



