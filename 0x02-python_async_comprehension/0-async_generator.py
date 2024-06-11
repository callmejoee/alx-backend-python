#!/usr/bin/env python3
''' module 1'''

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' function that waits for 1 sec'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
