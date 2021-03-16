#!/usr/bin/env python3
""" complex types - functions """

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    ''' duck type '''

    return lambda x: multiplier * x
