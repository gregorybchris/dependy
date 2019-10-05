import os

from dependy.logging import logging_utilities
from dependy.parsing import regex_utils
from dependy.structure.package_file import PackageFile
from dependy.structure.package_item import PackageItem
from dependy.structure.dependency_graph import DependencyGraph


class DependencyParser:
    FILE_SIZE_LIMIT = 1000000000

    def __init__(self, package_name, package_path, logger=None):
        if not os.path.isdir(package_path):
            raise IOError(f"{package_path} not found.")

        self._package_name = package_name
        self._package_path = package_path
        self._graph = DependencyGraph()
        self._logger = logger if logger is not None else logging_utilities.get_logger()

    def parse(self):
        self._logger.info(f'Loading: {self._package_name}...')
        print(f'Loading: {self._package_name}...')
        self._parse_path(self._package_path)

    def _parse_path(self, path):
        for root, module_names, file_names in os.walk(path):
            for name in module_names:
                print(f"Skipping module: {name}")
            for name in file_names:
                if not regex_utils.is_python_filename(name):
                    continue

                path = os.path.join(root, name)
                self._validate_duplicate(path)
                # TODO: Check if directory before checking size
                self._validate_file_size(path)
                self._create_file(name, path)

    def _validate_duplicate(self, path):
        key = PackageItem.get_path_key(path)
        if key in self._graph:
            raise ValueError(f"{path} already exists in package.")

    def _validate_file_size(self, path):
        n_bytes = os.stat(path).st_size
        if n_bytes > DependencyParser.FILE_SIZE_LIMIT:
            raise OSError(f"File {path} too large to parse.")

    def _create_module(self, name, path):
        # TODO: Handle creating a module
        pass

    def _create_file(self, name, path):
        package_file = PackageFile(name, path)
        self._graph.add_item(package_file)

        with open(path) as f:
            lines = [line.rstrip() for line in f.readlines()]
        for line in lines:
            import_path = regex_utils.extract_path_from_line(line)
            if import_path is not None:
                self._extract_from_import(import_path)

    def _extract_from_import(self, import_line):
        pass
