import hashlib

from dependy.parsing import regex_utils

from abc import ABC

class PackageItem(ABC):
    def __init__(self, name, path):
        self._name = name
        self._path = path
        self._key = PackageItem.get_path_key(path)

    def get_name(self):
        return self._name

    def get_path(self):
        return self._path

    def get_key(self):
        return self._key

    @staticmethod
    def get_path_key(path):
        return hashlib.md5(path.encode()).hexdigest()
