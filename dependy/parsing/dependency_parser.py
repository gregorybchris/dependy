import json
import os

from dependy.core import settings
from dependy.logging import logging_utilities
from dependy.parsing import regex_utilities
from dependy.structure.package_file import PackageFile
from dependy.structure.dependency_graph import DependencyGraph


class DependencyParser:
    FILE_SIZE_LIMIT = 1000000000

    def __init__(self, package_path, logger=None):
        if not os.path.isdir(package_path):
            raise IOError(f"{package_path} not found.")

        self._package_name = DependencyParser._get_dir_name(package_path)
        self._package_path = package_path
        self._graph = DependencyGraph()
        self._logger = logger if logger is not None else logging_utilities.get_logger()

    def parse(self):
        self._logger.info(f'Parsing package: {self._package_name}...')
        self._parse_path(self._package_path)

    @staticmethod
    def _get_dir_name(path):
        _, tail = os.path.split(path)
        return tail

    @staticmethod
    def _any_in(patterns, target):
        for pattern in patterns:
            if pattern in target:
                return True
        return False

    def _parse_path(self, path):
        for root, module_names, file_names in os.walk(path):
            to_ignore = ['__pycache__', 'static']
            if DependencyParser._any_in(to_ignore, root):
                continue

            # print("\nroot: ", root)
            # print("module_names: ", module_names)
            # print("file_names: ", file_names)

            for file_name in file_names:
                # print("Processing file: ", file_name)
                if not regex_utilities.is_python_filename(file_name):
                    continue

                file_path = os.path.join(root, file_name)
                # self._validate_duplicate(file_path)
                self._validate_file_size(file_path)
                self._register_file(file_name, file_path)

            for module_name in module_names:
                # print("Processing module: ", module_name)
                module_path = os.path.join(root, module_name)
                self._register_module(module_name, module_path)

    def _validate_file_size(self, path):
        n_bytes = os.stat(path).st_size
        if n_bytes > DependencyParser.FILE_SIZE_LIMIT:
            raise OSError(f"File {path} too large to parse.")

    def _register_module(self, name, path):
        # TODO: Handle creating a module
        # This will not be part of the dependency graph,
        # but it will be part of the file tree
        pass

    def _register_file(self, name, path):
        package_file = PackageFile(name, path)
        if not package_file.get_key() in self._graph:
            self._graph.add_item(package_file)

        with open(path) as f:
            lines = [line.rstrip() for line in f.readlines()]
        for line in lines:
            import_path = regex_utilities.extract_path_from_line(line)
            if import_path is not None:
                # TODO: Include all external dependencies
                if not import_path.startswith(self._package_name):
                    continue

                path_to_package = os.path.split(self._package_path)[0]
                print('\npath_to_package', path_to_package)
                dependency_path = os.path.join(path_to_package, import_path)
                print('dependency_path', dependency_path)
                dependency_name = DependencyParser._get_dir_name(dependency_path)
                print('dependency_name', dependency_name)
                dependency_file = PackageFile(dependency_name, dependency_path)
                if not dependency_file.get_key() in self._graph:
                    self._graph.add_item(dependency_file)
                self._graph.add_dependency(package_file, dependency_file)

    def save_graph(self, filename=settings.DEPENDY_GRAPH_FILE, cache_path=settings.DEPENDY_CACHE):
        graph_dict = self._graph.serialize()
        graph_json = json.dumps(graph_dict)
        path = os.path.join(cache_path, filename)
        with open(path, 'w') as f:
            f.write(graph_json)
