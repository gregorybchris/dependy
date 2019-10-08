from dependy.visualization.serving.app import App
from dependy.visualization.visualization_config import VisualizationConfig


class Visualizer:
    def __init__(self, config=None, logger=None):
        self._config = config if config is not None else VisualizationConfig()
        self._app = App(self._config, logger=logger)

    def start(self):
        self._app.run()
