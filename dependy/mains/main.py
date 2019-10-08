import argparse

from dependy.core.dependy_config import DependyConfig
from dependy.parsing.dependency_parser import DependencyParser
from dependy.visual.visualizer import Visualizer


DEFAULT_GRAPH_FILE = 'graph.json'
DEFAULT_PORT = 5000

MODE_ALL = 'all'
MODE_PARSE = 'parse'
MODE_VISUALIZE = 'viz'

ALL_MODES = [MODE_ALL, MODE_PARSE, MODE_VISUALIZE]


def parse(config, project_path):
    parser = DependencyParser(project_path, config=config)
    parser.parse_dependencies()


def visualize(config):
    visualizer = Visualizer(config=config)
    visualizer.start()


def run():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--filename', '-f', default=DEFAULT_GRAPH_FILE,
                        help='Filename for the graph.')
    parser.add_argument('--port', default=DEFAULT_PORT,
                        help='Port for the server.')
    parser.add_argument('--debug', default=False, action='store_true',
                        help='Whether to run the server in debug mode.')
    parser.add_argument('--mode', '-m', choices=ALL_MODES, default=MODE_ALL,
                        help='Running mode to use.')
    parser.add_argument('--project_path', '-p', help='Running mode to use.', required=True)
    args = parser.parse_args()

    config = DependyConfig(graph_filename=args.filename, port=args.port, debug=args.debug)
    if args.mode == MODE_ALL or args.mode == MODE_PARSE:
        parse(config, args.project_path)
    if args.mode == MODE_ALL or args.mode == MODE_VISUALIZE:
        visualize(config)
