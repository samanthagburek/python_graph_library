from ._booty_boost import Graph as _Graph
from .interface import BaseGraph


class Graph(BaseGraph):
    def __init__(self) -> None:
        self.g = _Graph()

    def add_edge(self, node1: str, node2: str):
        return self.g.add_edge(node1, node2)

    def bfs(self, node: str):
        return self.g.bfs(node)

    def dfs(self, node: str):
        return self.g.dfs(node)
