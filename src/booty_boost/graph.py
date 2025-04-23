from ._booty_boost import Graph as _Graph
from .interface import BaseGraph


class Graph(BaseGraph):
    """
    A wrapper around a Boost-based graph implementation providing
    basic graph operations like BFS, DFS, and tree checking.
    """
    def __init__(self) -> None:
        """
        Initializes a new empty graph.
        """
        self.g = _Graph()

    def add_node(self, node: str) -> bool:
        """
        Adds a node to the graph if it doesn't already exist.

        Args:
            node (str): The label of the node to add.

        Returns:
            bool: True if the node was added, False if it already existed.
        """
        return self.g.add_node(node)

    def add_edge(self, node1: str, node2: str) -> bool:
        """
        Adds an undirected edge between two nodes. Nodes are created if they don't exist.

        Args:
            node1 (str): Label of the first node.
            node2 (str): Label of the second node.

        Returns:
            bool: True if the edge was added, False if it already existed.
        """
        return self.g.add_edge(node1, node2)

    def bfs(self, node: str):
        """
        Performs a breadth-first search starting from the given node.

        Args:
            node (str): The starting node label.

        Returns:
            List[str]: A list of node labels in the order they were visited.
        """
        return self.g.bfs(node)

    def dfs(self, node: str):
        """
        Performs a depth-first search starting from the given node.

        Args:
            node (str): The starting node label.

        Returns:
            List[Tuple[str, str]]: A list of edges (as tuples) in the DFS tree.
        """
        return self.g.dfs(node)

    def is_tree(self):
        """
        Checks whether the graph is a tree.

        Returns:
            bool: True if the graph is connected and acyclic (i.e. a tree), False otherwise.
        """
        return self.g.is_tree()
    
    def print_graph(self):
        """
        Prints the graph's adjacency list representation to standard output.
        """
        return self.g.print_graph()
