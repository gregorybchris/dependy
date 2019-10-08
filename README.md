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
from dependy.parsing.parsing_config import ParsingConfig
from dependy.parsing.dependency_parser import DependencyParser

config = ParsingConfig(graph_filename='graph.json')
parser = DependencyParser('full/path/to/my/package', config=config)
parser.parse_dependencies()
```

### Visualize that graph in the browser
```python
from dependy.visualization.visualization_config import VisualizationConfig
from dependy.visualization.visualizer import Visualizer

config = VisualizationConfig(port=5000, debug=True, graph_filename='graph.json')
visualizer = Visualizer(config=config)
visualizer.start()
```

## Complete

- [x] Graph visualization in the browser

## Future

- [ ] Multi-package support
- [ ] Hierarchical dependency tracking
- [ ] Make app interactive
