import os
import re


def is_python_filename(name):
    result = re.match(r'[a-zA-Z0-9_]+\.py', name)
    return bool(result)


def extract_path_from_line(line):
    def dotpath(line):
        return line.replace('.', os.sep)

    search = re.search(r'^import ([a-z0-9_\.]+)$', line)
    if search:
        return search.group(1).replace('.', os.sep)

    search = re.search(r'^from ([a-z0-9_\.]+) import ([a-zA-Z0-9_]+)$', line)
    if search:
        return os.path.join(dotpath(search.group(1)), dotpath(search.group(2)))

    return None
