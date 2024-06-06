#!/usr/bin/env python3
''' Task 5 module '''


def sum_list(input_list: list[float]) -> float:
    ''' function to sum floats into one int '''
    result = 0
    for num in input_list:
        result += num
    return result
