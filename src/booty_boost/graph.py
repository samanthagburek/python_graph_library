from ._booty_boost import Graph as _Graph
from .interface import BaseGraph


class Graph(BaseGraph):
    """
    A wrapper around a Boost-based graph implementation providing
    basic graph operations like BFS, DFS, and tree checking.
    """

    def __init__(self) -> None:
        self.g = _Graph()

    def add_node(self, node: str) -> bool:
        return self.g.add_node(node)

    def add_edge(self, node1: str, node2: str) -> bool:
        return self.g.add_edge(node1, node2)

    def bfs(self, node: str):
        return self.g.bfs(node)

    def dfs(self, node: str):
        return self.g.dfs(node)

    def is_tree(self):
        return self.g.is_tree()

    def print_graph(self):
        return self.g.print_graph()
