import flask
import pkg_resources

from dependy.core import settings


class App:
    def __init__(self, config):
        self._config = config

        self._app = flask.Flask(__name__, static_url_path='')
        self._register_routes()

    def _register_routes(self):
        self._app.route('/static/<path:path>', methods=['GET'])(App.get_static)
        self._app.route('/', methods=['GET'])(App.get_index)
        self._app.route('/info', methods=['GET'])(App.get_app_info)

    @staticmethod
    def get_static(path):
        return flask.send_from_directory('static', path)

    @staticmethod
    def get_index():
        return flask.current_app.send_static_file('pages/index.html')

    @staticmethod
    def get_app_info():
        info = {
            'version': pkg_resources.get_distribution("dependy").version,
            'author': 'Chris Gregory',
            'package': 'dependy',
            'license': 'Apache Software License'
        }
        return flask.jsonify(info)

    def run(self, host='localhost', port=None, debug=None):
        if port is None:
            port = settings.FLASK_RUN_PORT

        if debug is None:
            debug = settings.FLASK_DEBUG

        self._app.run(host=host, port=port, debug=debug)
