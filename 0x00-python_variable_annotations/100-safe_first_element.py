#!/usr/bin/env python3
""" 10. Duck typing """

from typing import Any
from typing import Sequence
from typing import Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' first element of a sequence '''
    if lst:
        return lst[0]
    else:
        return None
