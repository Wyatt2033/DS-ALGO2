# Graph class
class Graph:

    # Graph object creation.
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    # Adds a vertex to the graph object adjacency list.
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    # Adds a directed edge to the graph.
    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    # Adds an undirected edge to the graph.
    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)