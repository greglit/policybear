#!/usr/bin/python3
"""
Created Mar 23, 2021

Parameter specifications
"""
from ..metadata.specs import param_specs
from ..metadata.specs import ParamSpecs

benchmarks = {
    'cows': 100*0.001*23,
    'cars': 110*1e-6*12000
}

class CompareTo:
    def __init__(self,ParamSpecs,change,benchmarks,compare_to):
        self.PS = ParamSpecs
        self.co2eq_factor = self.PS.co2eq
        self.change = change
        self.benchmarks = benchmarks
        self.compare = compare_to
        self.value = self.benchmarks[self.compare]

    def co2eq(self):
        return self.change * self.co2eq_factor

    def air_mass_arctic(self):
        areafrac_arctic = 3700000 / 510000000
        mass_global = 5.13 * 10 ** 15
        mass_arctic = mass_global * areafrac_arctic
        tons = round((self.co2eq() * 1e-06 * mass_arctic), 3)  # gt 1e-9
        return tons

    def calc(self):
        return round(self.air_mass_arctic() / self.value)