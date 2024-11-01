#!/usr/bin/env python3
"""
Module that provides MRUCache class.
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRU Caching system.
    """
    def __init__(self):
        """
        Initialize parent class
        """
        super().__init__()

        # Initialize a list to keep track of the order of keys for MRU
        self.access_order = []

    def put(self, key, item):
        """
        Assign item value to a key in the dictionary.
        If the cache exceeds MAX_ITEMS, remove the most recently
        used item (MRU).
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.access_order.append(key)

        # Check if we need to discard the last item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.access_order.pop(-2)
            del self.cache_data[discard]
            print(f"DISCARD: {discard}")

    def get(self, key):
        """
        Return value in the dictionary by key,
        and update it as the most recently used.
        """
        if key is None or key not in self.cache_data:
            return None

        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data.get(key)
