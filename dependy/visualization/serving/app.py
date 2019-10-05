import flask
import json
import os
import pkg_resources

from dependy.core import settings
from dependy.logging import logging_utilities
from dependy.visualization.serving.codes import HTTPCodes


class App:
    def __init__(self, config, logger=None):
        self._config = config
        self._logger = logger if logger is not None else logging_utilities.get_logger()

        self._app = flask.Flask(__name__, static_url_path='')
        self._register_routes()
        self._register_api_endpoints()

    def _register_routes(self):
        self._app.route('/', methods=['GET'])(self.get_index)
        self._app.route('/static/<path:path>', methods=['GET'])(self.get_static_resource)

    def _register_api_endpoints(self):
        self._app.route('/api/info', methods=['GET'])(self.api_get_info)
        self._app.route('/api/config', methods=['GET'])(self.api_get_config)
        self._app.route('/api/graph', methods=['GET'])(self.api_get_graph)

    def get_index(self):
        return flask.current_app.send_static_file('pages/index.html')

    def get_static_resource(self, path):
        return flask.send_from_directory('static', path)

    @logging_utilities.log_context('get_info', context_tag='api_log')
    def api_get_info(self):
        info = {
            'author': 'Chris Gregory',
            'index': 'https://pypi.org/project/dependy/',
            'license': 'Apache Software License',
            'package': 'dependy',
            'source': 'https://github.com/gregorybchris/dependy',
            'version': pkg_resources.get_distribution("dependy").version
        }
        return flask.jsonify(info)

    @logging_utilities.log_context('get_config', context_tag='api_log')
    def api_get_config(self):
        return flask.jsonify(self._config.serialize())

    @logging_utilities.log_context('get_graph', context_tag='api_log')
    def api_get_graph(self):
        graph_path = os.path.join(settings.DEPENDY_CACHE, settings.DEPENDY_GRAPH_FILE)
        if not os.path.exists(graph_path):
            self._logger.warn("Graph file not found")
            return App.error('Graph file not found', HTTPCodes.ERROR_NOT_FOUND)
        with open(graph_path, 'r') as f:
            graph = json.load(f)
        return flask.jsonify(graph)

    @staticmethod
    def error(message, code):
        return (flask.jsonify(message=str(message)), code)

    def run(self, host='localhost', port=None, debug=None):
        if port is None:
            port = settings.FLASK_RUN_PORT

        if debug is None:
            debug = settings.FLASK_DEBUG

        self._app.run(host=host, port=port, debug=debug)
