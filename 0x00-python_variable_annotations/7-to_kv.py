#!/usr/bin/env python3
''' Task 7 module '''

from typing import Tuple, Union
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    '''
    Function to return a tuple with the key and the square root of the value
    '''
    return (k, math.sqrt(v))
