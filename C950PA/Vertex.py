# Vertex class.
class Vertex:
    # Creates vertex object.
    def __init__(self, ID):
        self.ID = ID
        self.distance = float('inf')
        self.pred_vertex = None
