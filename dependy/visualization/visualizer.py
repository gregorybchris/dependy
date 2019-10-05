from dependy.logging import logging_utilities
from dependy.visualization.serving.app import App


class Visualizer:
    def __init__(self, config, logger=None):
        self._logger = logger if logger is not None else logging_utilities.get_dependy_logger()
        self._app = App(config, logger=logger)

    def start(self):
        self._app.run()
