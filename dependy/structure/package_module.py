from dependy.structure.package_item import PackageItem


class PackageModule(PackageItem):
    def __init__(self, name, path):
        super(PackageModule, self).__init__(name, path)
        self._items = []

    def add_item(self, item):
        # TODO: Check for item actually being in module
        self._items.append(item)
