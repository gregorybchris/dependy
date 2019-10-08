class VisualizationConfig:
    def __init__(self,
                 host=None,
                 port=None,
                 debug=None,
                 graph=None):
        self.host = host
        self.port = port
        self.debug = debug
        self.graph = graph

    def serialize(self):
        return {
            'host': self.host,
            'port': self.port,
            'debug': self.debug,
            'graph': self.graph
        }
