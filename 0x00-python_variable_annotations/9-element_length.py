#!/usr/bin/env python3
''' Task 7 module '''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Function to return a list of tuples containing elements and their lengths
    '''
    return [(i, len(i)) for i in lst]
