#!/usr/bin/env python3
""" 4. MRU caching
  - basic cache with 'most recently used' replacement method.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Class demonstrating an MRU caching method.
    """
    def __init__(self):
        """ init class
          - @keyList: to keep track of order of requests.
        """
        super().__init__()
        self.keyList = []

    def put(self, key, item):
        """ add record to cache
          - while keeping track of the order of requests for each record
          - @mostKey: the key used most recently
        """
        if key and item:
            if key in self.cache_data:
                del self.cache_data[key]
                self.keyList.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    mostKey = self.keyList[-1]
                    del self.cache_data[mostKey]
                    self.keyList.remove(mostKey)
                    print("DISCARD:", mostKey)
            self.keyList.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get record from cache
          - add key to keyList to track least recent requests.
        """
        if key and key in self.cache_data:
            self.keyList.remove(key)
            self.keyList.append(key)
            return self.cache_data[key]
        return None
