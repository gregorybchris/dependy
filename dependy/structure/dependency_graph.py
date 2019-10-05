import json


class DependencyGraph:
    def __init__(self):
        self._items = dict()
        self._dependencies = dict()

    def add_item(self, item):
        key = item.get_key()
        self._items[key] = item
        self._dependencies[key] = dict()

    def __contains__(self, key):
        return key in self._items

    def has_item(self, item):
        key = item.get_key()
        return key in self._items

    def add_dependency(self, item_a, item_b):
        key_a, key_b = item_a.get_key(), item_b.get_key()
        if key_a not in self._items:
            raise ValueError("Argument item_a not found in the dependency graph.")
        if key_b not in self._items:
            raise ValueError("Argument item_b not found in the dependency graph.")

        self._dependencies[key_a][key_b] = item_b

    def to_json(self):
        return json.dumps(self._dependencies)
