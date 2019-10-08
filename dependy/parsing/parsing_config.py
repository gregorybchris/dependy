class ParsingConfig:
    def __init__(self,
                 graph_filename=None,
                 cache_path=None):
        self.graph_filename = graph_filename
        self.cache_path = cache_path

    def serialize(self):
        return {
            'graph_filename': self.graph_filename,
            'cache_path': self.cache_path
        }
