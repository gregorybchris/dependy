class VisualizationConfig:
    def __init__(self, graph=None):
        self.graph = graph

    def serialize(self):
        return {
            'graph': self.graph
        }
