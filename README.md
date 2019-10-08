# Dependy

[![codecov](https://codecov.io/gh/gregorybchris/dependy/branch/master/graph/badge.svg?token=1kwR72lEIQ)](https://codecov.io/gh/gregorybchris/dependy)

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
from dependy.core.dependy_config import DependyConfig
from dependy.parsing.dependency_parser import DependencyParser
from dependy.visual.visualizer import Visualizer

# Create a configuration to be used by dependy
config = DependyConfig(graph_filename='graph.json', port=5000, debug=False)

# Parse the files of your package into a dependy graph
parser = DependencyParser('full/path/to/my/package', config=config)
parser.parse_dependencies()

# Visualize the dependency graph in the browser
visualizer = Visualizer(config=config)
visualizer.start()
```

## Complete

- [x] Graph visualization in the browser

## Future

- [ ] Multi-package support
- [ ] Hierarchical dependency tracking
- [ ] Make app interactive
