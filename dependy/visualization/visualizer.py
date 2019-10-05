from dependy.visualization.serving.app import App


class Visualizer:
    def __init__(self, config):
        self._app = App(config)

    def start(self):
        self._app.run()
