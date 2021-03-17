#!/usr/bin/env python3
"""  """

import asyncio
import random
import typing


async def wait_n(n: int = 0, max_delay: int = 10) -> typing.List[float]:
    """ """

    wait_random = __import__('0-basic_async_syntax').wait_random

    delays: typing.List[float] = []
    routines: typing.List = []

    for i in range(n):
        routines.append(wait_random(max_delay))

    for routine in asyncio.as_completed(routines):
        delays.append(await routine)

    return delays
