#!/usr/bin/env python3
"""basic cache"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Basic cache implemented"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """updating the cache_data"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            mru = list(self.cache_data.keys())[-2]
            del self.cache_data[mru]
            print(f"DISCARD: {mru}")

    def get(self, key):
        """get the value associated with the key"""
        if key is None or key not in self.cache_data:
            return None
        if key in self.cache_data:
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
        return self.cache_data[key]
