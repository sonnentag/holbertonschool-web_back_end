#!/usr/bin/env python3
""" 7. Complex types """

from typing import Tuple
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' string and int/float to tuple '''

    return (k, v ** 2)
