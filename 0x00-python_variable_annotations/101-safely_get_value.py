#!/usr/bin/env python3
""" 11. More involved type annotations """

from typing import Any
from typing import Mapping
from typing import TypeVar
from typing import Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    ''' demonstrating typevar and annotations '''
    if key in dct:
        return dct[key]
    else:
        return default
