#!/usr/bin/env python3
""" 0. Async Generator """

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' comprehend data generated in task 0 '''

    return [i async for i in async_generator()]
