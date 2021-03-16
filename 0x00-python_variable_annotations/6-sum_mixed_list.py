#!/usr/bin/env python3
""" sum list of floats """

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    ''' '''

    return sum(list(mxd_lst))
