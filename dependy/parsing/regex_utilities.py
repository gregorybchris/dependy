import os
import re


def is_python_filename(name):
    result = re.match(r'[a-zA-Z0-9_]+\.py', name)
    return bool(result)


def extract_path_from_line(line):
    def dotsep(line):
        return line.replace('.', os.path.sep)

    def topy(path):
        return f'{path}.py'

    search = re.search(r'^import ([a-z0-9_\.]+)$', line)
    if search:
        return topy(dotsep(search.group(1)))

    search = re.search(r'^from ([a-z0-9_\.]+) import ([a-zA-Z0-9_]+)$', line)
    if search:
        if search.group(2)[0].isupper():
            return topy(dotsep(search.group(1)))
        else:
            return topy(os.path.join(dotsep(search.group(1)), dotsep(search.group(2))))

    return None
