#!/usr/bin/env python3
"""basic cache"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Basic cache implemented"""
    def __init__(self):
        super().__init__()
        self.keep_track = None

    def put(self, key, item):
        """updating the cache_data"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.keep_track = key
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            if self.keep_track:
                del self.cache_data[self.keep_track]
                print(f"DISCARD: {self.keep_track}")
                self.keep_track = None
            else:
                last = list(self.cache_data.keys())[-2]
                del self.cache_data[last]
                print(f"DISCARD: {last}")

    def get(self, key):
        """get the value associated with the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
