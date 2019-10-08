class VisualizationConfig:
    def __init__(self,
                 port=None,
                 debug=None,
                 graph_filename=None):
        self.port = port
        self.debug = debug
        self.graph_filename = graph_filename

    def serialize(self):
        return {
            'port': self.port,
            'debug': self.debug,
            'graph_filename': self.graph_filename
        }
