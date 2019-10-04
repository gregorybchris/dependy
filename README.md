# Dependy

Dependy is a dependency grapher for Python projects. Use this tool to efficiently restructure code and clean up dependencies.

## Installation

Install the current PyPI release:

```python
pip install dependy
```

Or install from source:

```python
pip install git+https://github.com/gregorybchris/dependy
```

## Usage

```python
from dependy.parsing.dependency_parser import DependencyParser

parser = DependencyParser('<package-name>', '<path-to-package>')
parser.parse()
```

## Future

- [ ] Multi-package support
- [ ] Hierarchical dependency tracking
- [ ] Graph visualization in the browser
