class DependyConfig:
    def __init__(self,
                 port=None,
                 debug=None,
                 graph_filename=None,
                 cache_path=None):
        self.port = port
        self.debug = debug
        self.graph_filename = graph_filename
        self.cache_path = cache_path

    def serialize(self):
        return {
            'port': self.port,
            'debug': self.debug,
            'graph_filename': self.graph_filename,
            'cache_path': self.cache_path
        }
