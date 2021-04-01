#!/usr/bin/python3
"""
Created Mar 23, 2021

Parameter specifications
"""

param_specs = {
    'ch4': {'dataset': 'ICOS ATC NRT CH4 growing time series',
            'label': 'ch4',
            'variable': None,
            'access_folders': None,
            'type': 'CH4 mixing ratio (dry mole fraction, ppb)',
            'unit': 'nmol mol-1',
            'unit_conv': 0.001,
            'dst_unit': 'ppm',
            'category': 'gas',
            'co2eq_factor': 23,
            'round_decimals': 2},

    'co2': {'dataset': 'ICOS ATC NRT CO2 growing time series',
            'label': 'co2',
            'variable': None,
            'access_folders': None,
            'type': 'CO2 mixing ratio (dry mole fraction, ppm)',
            'unit': 'µmol mol-1',
            'unit_conv': 1,
            'dst_unit': 'ppm',
            'category': 'gas',
            'co2eq_factor': 1,
            'round_decimals': 2},

    'sic': {'dataset': 'ssmi-ssmis-hydrological-products',
            'label': 'mw-hydro_v01_2.5-deg_ice_early',
            'variable': 'sea_ice_cover',
            'access_folders': 'access/netcdf/',
            'type': None,
            'unit': None,
            'unit_conv': None,
            'dst_unit': None,
            'category': 'area',
            'co2eq_factor': None,
            'round_decimals': None}
}

class ParamSpecs:
    def __init__(self,param, param_specs):
        self.param = param
        self.specs = param_specs

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


