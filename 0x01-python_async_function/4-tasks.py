#!/usr/bin/env python3

''' Q1 Module '''

import asyncio
from typing import List


wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' Executes wait_random number n times '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
