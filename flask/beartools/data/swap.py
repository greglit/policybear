#!/usr/bin/python3
"""
Created May 28, 2021

Data swap control.
"""
import sys
import math
import numpy as np

def inspect_data_swap(data_swap):
    size = np.sum([sys.getsizeof(v)/1024**2 for v in data_swap.values()])
    print(f'Swap | inspect data swap | '
          f'Size of Dictionary below {math.ceil(size)} ({round(size,2)})')