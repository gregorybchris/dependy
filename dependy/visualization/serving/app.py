import flask
import pkg_resources

from dependy.core import settings


class App:
    def __init__(self, config):
        self._config = config

        self._app = flask.Flask(__name__, static_url_path='')
        self._register_routes()
        self._register_api_endpoints()

    def _register_routes(self):
        self._app.route('/', methods=['GET'])(self.get_index)
        self._app.route('/static/<path:path>', methods=['GET'])(self.get_static_resource)

    def _register_api_endpoints(self):
        self._app.route('/api/config', methods=['GET'])(self.api_get_config)
        self._app.route('/api/info', methods=['GET'])(self.api_get_app_info)

    def get_index(self):
        return flask.current_app.send_static_file('pages/index.html')

    def get_static_resource(self, path):
        return flask.send_from_directory('static', path)

    def api_get_config(self):
        return flask.jsonify(self._config.serialize())

    def api_get_app_info(self):
        info = {
            'author': 'Chris Gregory',
            'index': 'https://pypi.org/project/dependy/',
            'license': 'Apache Software License',
            'package': 'dependy',
            'source': 'https://github.com/gregorybchris/dependy',
            'version': pkg_resources.get_distribution("dependy").version
        }
        return flask.jsonify(info)

    def run(self, host='localhost', port=None, debug=None):
        if port is None:
            port = settings.FLASK_RUN_PORT

        if debug is None:
            debug = settings.FLASK_DEBUG

        self._app.run(host=host, port=port, debug=debug)
