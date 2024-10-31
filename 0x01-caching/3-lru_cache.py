#!/usr/bin/env python3
"""
Module that provides LRUCache class.
"""

BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LIFO Caching system.
    """
    def __init__(self):
        """
        Initialize parent class
        """
        super().__init__()
        # Initialize a list to keep track of the order of keys for LRU
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assign item value to a key in the dictionary.
        If the cache exceeds MAX_ITEMS, remove the least recently
        used item (LRU).
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)
        self.cache_data[key] = item

        # Check if we need to discard the last item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard, _ = self.cache_data.popitem(last=False)

            print(f"DISCARD: {discard}")

    def get(self, key):
        """
        Return value in the dictionary by key,
        and update it as the most recently used.
        """
        if key is None or key not in self.cache_data:
            return None
        
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
