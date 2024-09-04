#!/usr/bin/env python3
"""basic cache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic cache implemented"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """updating the cache_data"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get the value associated with the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
