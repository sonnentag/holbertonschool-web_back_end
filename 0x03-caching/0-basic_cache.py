#!/usr/bin/env python3
""" 0. Basic dictionary
  - Basic get/put. No replacement/expiration or MAXSIZE/MAX_ITEMS.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' Class demonstrating a basic caching system
    '''
    def put(self, key, item):
        ''' add record to cache
        '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        ''' get record from cache
        '''
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
