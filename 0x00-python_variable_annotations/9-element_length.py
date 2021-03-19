#!/usr/bin/env python3
"""  9. Let's duck type an iterable object """

from typing import Iterable
from typing import List
from typing import Sequence
from typing import Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' duck type '''

    return [(i, len(i)) for i in lst]
