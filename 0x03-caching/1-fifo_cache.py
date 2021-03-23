#!/usr/bin/env python3
""" 1. FIFO caching
  - basic cache with 'first in/first out' replacement method.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' Class demonstrating a basic FIFO method.
    '''
    def put(self, key, item):
        """ add record to cache
          - if MAX_ITEMS is reached the oldest record will be removed
        """
        if key and item:
            if key in self.cache_data:
                del self.cache_data[key]
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    lastKey = next(iter(self.cache_data))
                    del self.cache_data[lastKey]
                    print("DISCARD:", lastKey)
            self.cache_data[key] = item

    def get(self, key):
        """ get record from cache
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
