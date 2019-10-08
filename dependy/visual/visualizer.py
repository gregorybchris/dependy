from dependy.core.dependy_config import DependyConfig
from dependy.visual.serving.app import App


class Visualizer:
    def __init__(self, config=None, logger=None):
        self._config = config if config is not None else DependyConfig()
        self._app = App(self._config, logger=logger)

    def start(self):
        self._app.run()
