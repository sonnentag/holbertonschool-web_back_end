#!/usr/bin/env python3
""" 2. LIFO caching
  - basic cache with 'last in/first out' replacement method.
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Class demonstrating a basic LIFO method.
    """
    def __init__(self):
        """ init class
        """
        super().__init__()
        self.keyList = []

    def put(self, key, item):
        """ add record to cache
        """
        if key and item:
            if key in self.cache_data:
                del self.cache_data[key]
                self.keyList.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    leastKey = self.keyList[0]
                    del self.cache_data[leastKey]
                    self.keyList.remove(leastKey)
                    print("DISCARD:", leastKey)
            self.keyList.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get record from cache
        """
        if key and key in self.cache_data:
            self.keyList.remove(key)
            self.keyList.append(key)
            return self.cache_data[key]
        return None
