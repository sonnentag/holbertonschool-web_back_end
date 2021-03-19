#!/usr/bin/env python3
""" 2. Measure the runtime """

import asyncio
import time


def measure_time(n: int, max_delay: int = 10) -> float:
    """ measure the runtime """

    wait_n = __import__('1-concurrent_coroutines').wait_n

    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    return ((end - start) / n)
