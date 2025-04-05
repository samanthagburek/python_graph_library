import graph_library as gl

class GraphLibrary:
    def __init__(self):
        self.graph = gl.Graph()

    def add_edge(self, u, v):
        self.graph.add_edge(u, v)

    def get_neighbors(self, node):
        return self.graph.get_neighbors(node)

    def run_dfs(self, start):
        dfs = gl.GraphDFS()
        return dfs.execute(self.graph, start)

    def run_scc(self, start):
        scc = gl.GraphSCC()
        return scc.execute(self.graph, start)

    def run_shortest_path(self, start):
        sp = gl.GraphShortestPath()
        return sp.execute(self.graph, start)

