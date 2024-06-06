#!/usr/bin/env python3
''' Task 7 module '''

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Func to return a tuple with the key and the square of the value as float
    '''
    return (k, float(v**2))
