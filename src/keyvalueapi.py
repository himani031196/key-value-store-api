import json
from keyvaluestore import KeyValueStore

class KeyValueApi():
    def __init__(self):
        self.kv = KeyValueStore()
    
    def homepage(self):
        return "This is an implementation of Key Value Store"

    def set_items(self, key, value):
        self.kv.setitem(key, value)
        return "Data Added Successfully"

    def get_key_value(self, key):
        return self.kv.getitem(key)

    def search_prefix_in_key(self, prefix):
        results = []
        results = [ key for key in self.kv.iterkeys() if key.startswith(prefix)]
        return results if results is not None else 0

    def search_suffix_in_key(self, suffix):
        results = []
        results = [ key for key in self.kv.iterkeys() if key.endswith(suffix)]
        return results if results is not None else 0

    def __del__(self):
        self.kv.close()
