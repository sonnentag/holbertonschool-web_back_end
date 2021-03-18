#!/usr/bin/env python3
""" 2. Run time for four parallel comprehensions """

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' gauge parallel runtime of previous task '''

    sTime = time.perf_counter()

    genData = [async_comprehension() for _ in range(4)]

    await asyncio.gather(*genData)

    eTime = time.perf_counter()

    return (eTime - sTime)
