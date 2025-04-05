import graph_backend

class GraphLibrary:
    def __init__(self):
        self.graph = graph_backend.Graph()

    def add_edge(self, u, v):
        self.graph.add_edge(u, v)

    def get_neighbors(self, node):
        return self.graph.get_neighbors(node)

    def run_dfs(self, start):
        dfs = graph_backend.GraphDFS()
        return dfs.execute(self.graph, start)

    def run_scc(self, start):
        scc = graph_backend.GraphSCC()
        return scc.execute(self.graph, start)

    def run_shortest_path(self, start):
        sp = graph_backend.GraphShortestPath()
        return sp.execute(self.graph, start)

