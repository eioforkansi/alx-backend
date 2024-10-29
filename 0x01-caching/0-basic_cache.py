#!/usr/bin/env python3
"""
Module that provides BaseCache class.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Caching system.
    """
    def __init__(self):
        """
        Initialize parent class
        """
        super().__init__()

    def put(self, key, item):
        """
        Assign value to a key in the dictionary.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Return value in a the dictionary by key.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
