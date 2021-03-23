#!/usr/bin/env python3
""" 2. LIFO caching
  - basic cache with 'last in/first out' replacement method.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Class demonstrating a basic LIFO method.
    """
    def __init__(self):
        """ init class
          - @keyList: to keep track of keys in queue
        """
        super().__init__()
        self.keyList = []

    def put(self, key, item):
        """ add record to cache
          - if MAX_ITEMS is reached the newest record will be removed
        """
        if key and item:
            self.keyList.append(key)
            if key in self.cache_data:
                del self.cache_data[key]
                self.keyList.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    lastKey = self.keyList[-2]
                    del self.cache_data[lastKey]
                    self.keyList.remove(lastKey)
                    print("DISCARD:", lastKey)
            self.cache_data[key] = item

    def get(self, key):
        """ get record from cache
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
