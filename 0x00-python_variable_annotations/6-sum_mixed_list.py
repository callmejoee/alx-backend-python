#!/usr/bin/env python3
''' Task 5 module '''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Function to sum a list of integers and floats and return the sum as a float
    '''
    return sum(mxd_lst)
