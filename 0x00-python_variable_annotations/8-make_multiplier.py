#!/usr/bin/env python3
''' Task 7 module '''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Function to create a multiplier function
    '''
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
