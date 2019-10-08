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

### Create a graph representation of your package
```python
from dependy.core.dependy_config import DependyConfig
from dependy.parsing.dependency_parser import DependencyParser

config = DependyConfig(graph_filename='graph.json')
parser = DependencyParser('full/path/to/my/package', config=config)
parser.parse_dependencies()
```

### Visualize that graph in the browser
```python
from dependy.core.dependy_config import DependyConfig
from dependy.visualization.visualizer import Visualizer

config = DependyConfig(graph_filename='graph.json', port=5000, debug=True)
visualizer = Visualizer(config=config)
visualizer.start()
```

## Complete

- [x] Graph visualization in the browser

## Future

- [ ] Multi-package support
- [ ] Hierarchical dependency tracking
- [ ] Make app interactive
