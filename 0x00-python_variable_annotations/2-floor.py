#!/usr/bin/env python3
''' Task 2 module '''


def floor(n: float) -> int:
    ''' Function to return the floor of a floating-point number '''
    if n >= 0:
        return int(n)
    else:
        return int(n) - 1 if n != int(n) else int(n)
