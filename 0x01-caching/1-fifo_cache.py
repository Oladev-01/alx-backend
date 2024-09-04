#!/usr/bin/env python3
"""basic cache"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Basic cache implemented"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """updating the cache_data"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """get the value associated with the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
