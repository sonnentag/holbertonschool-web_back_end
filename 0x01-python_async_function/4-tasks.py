#!/usr/bin/env python3
""" 4. Tasks """

import asyncio
import typing


async def task_wait_n(n: int = 0, max_delay: int = 10) -> typing.List[float]:
    """ wait for tack """

    task_wait_random = __import__('3-tasks').task_wait_random

    delays: typing.List[float] = []
    routines: typing.List[asyncio, task] = []

    for i in range(n):
        routines.append(task_wait_random(max_delay))

    for routine in asyncio.as_completed((routines)):
        delays.append(await routine)

    return delays
