#!/usr/bin/env python3
''' Task 7 module '''

from typing import Sequence, Union


def safe_first_element(lst: Sequence) -> Union[None, Sequence]:
    '''
    Function to return the first element of a sequence or None if the sequence is empty
    '''
    if lst:
        return lst[0]
    else:
        return None    return [(i, len(i)) for i in lst]
