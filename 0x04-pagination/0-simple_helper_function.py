#!/usr/bin/env python3
""" 0. Simple helper function
"""


def index_range(page, page_size):
    """ return a tuple containing indexes
     -  corresponding to pagination parameters
    """
    start_index = ((page - 1) * page_size)
    end_index = page_size * page

    return (start_index, end_index)
