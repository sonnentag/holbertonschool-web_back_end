#!/usr/bin/env python3
""" 5. LFU caching
  - basic cache with 'least frequently used' replacement method.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Class demonstrating an LFU caching method.
    """
    def __init__(self):
        """ init class
          - @keyList: to keep track of order of requests.
        """
        super().__init__()
        self.keyList = {}

    def put(self, key, item):
        """ add record to cache
          - while keeping track of the order of requests for each record
          - @mostKey: the key used most recently
        """
        if key and item:
            if key in self.cache_data:
                del self.cache_data[key]
                self.keyList[key] += 1
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    lastKey = min(self.keyList, key=self.keyList.get)
                    del self.cache_data[lastKey]
                    del self.keyList[lastKey]
                    print("DISCARD:", lastKey)
                    self.keyList[key] = 1
                self.keyList[key] = 1
            self.cache_data[key] = item

    def get(self, key):
        """ get record from cache
          - add key to keyList to track least recent requests.
        """
        if key and key in self.cache_data:
            self.keyList[key] += 1
            return self.cache_data[key]
        return None
