#!/usr/bin/env python3
""" 1. Simple pagination
"""

import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Take the page info given and return a list with the data
        """
        assert all(isinstance(i, int) for i in [page, page_size]) and page > 0
        start, end = self.index_range(page, page_size)

        return (self.dataset()[start:end])

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """ return a tuple of indexes corresponding to pagination parameters
        """
        start = ((page - 1) * page_size)
        end = page_size * page

        return (start, end)
