#!/usr/bin/env python3
''' Task 5 module '''

from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' Function to sum a list of floats and return the sum as a float '''
    result = 0.0  # Initialize result as a float
    for num in input_list:
        result += num
    return result
