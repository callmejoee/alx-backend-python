#!/usr/bin/env python3
''' Task 7 module '''

from typing import Sequence, Union


def safe_first_element(lst: Sequence) -> Union[None, Sequence]:
    '''
    Func to return the first elem of a seq or None
    '''
    if lst:
        return lst[0]
    else:
        return None
