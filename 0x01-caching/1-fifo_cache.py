#!/usr/bin/env python3
"""
Module that provides FIFOCache class.
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Caching system.
    """
    def __init__(self):
        """
        Initialize parent class
        """
        super().__init__()
        # Initialize a list to keep track of the order of keys for FIFO
        self.keys = []

    def put(self, key, item):
        """
        Assign item value to a key in the dictionary.
        Deletes oldest item.
        """
        if key is None or item is None:
            return
        
        if key not in self.cache_data:
            self.keys.append(key)
        self.cache_data[key] = item

        # Check if we need to discard the oldest item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.keys.pop(0)
            # Remove it from the cache
            del self.cache_data[discard]
            print(f"DISCARD: {discard}")

    def get(self, key):
        """
        Return value in the dictionary by key.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
