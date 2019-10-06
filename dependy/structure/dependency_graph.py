class DependencyGraph:
    def __init__(self):
        self._items = dict()
        self._dependencies = dict()

    def __setitem__(self, key, item):
        self._items[key] = item

    def __getitem__(self, key):
        return self._items[key]

    def __contains__(self, key):
        return key in self._items

    def add_item(self, item):
        key = item.get_key()
        self._items[key] = item
        self._dependencies[key] = set()

    def has_item(self, item):
        key = item.get_key()
        return key in self._items

    def add_dependency(self, item_a, item_b):
        key_a, key_b = item_a.get_key(), item_b.get_key()
        if key_a not in self._items:
            raise ValueError("Argument item_a not found in the dependency graph.")
        if key_b not in self._items:
            raise ValueError("Argument item_b not found in the dependency graph.")

        self._dependencies[key_a].add(key_b)

    def serialize(self):
        nodes, links = [], []
        graph = {'nodes': nodes, 'links': links}

        for key, item in self._items.items():
            nodes.append({'id': item.get_name(), 'group': 1})

        for item_key, dependencies in self._dependencies.items():
            item = self._items[item_key]
            for dependency_key in dependencies:
                dependency = self._items[dependency_key]
                links.append({
                    'source': item.get_name(),
                    'target': dependency.get_name(),
                    'value': 1
                })
        return graph
