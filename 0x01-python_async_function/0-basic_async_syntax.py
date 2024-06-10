#!/usr/bin/env python3

''' Q1 Module '''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' async function that takes an int and returns the random
    delay time it waits as a float '''

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
