class BaseGraph:
    """
    Interface definition for a simple graph library providing
    basic graph operations like BFS, DFS, and tree checking.
    """

    def __init__(self) -> None:
        """
        Initializes a new empty graph.
        """
        pass

    def add_node(self, node: str) -> bool:
        """
        Adds a node to the graph if it doesn't already exist.

        Args:
            node (str): The label of the node to add.

        Returns:
            bool: True if the node was added, False if it already existed.
        """
        pass

    def add_edge(self, node1: str, node2: str) -> bool:
        """
        Adds an undirected edge between two nodes. Nodes are created if they don't exist.

        Args:
            node1 (str): Label of the first node.
            node2 (str): Label of the second node.

        Returns:
            bool: True if the edge was added, False if it already existed.
        """
        pass

    def bfs(self, node: str):
        """
        Performs a breadth-first search starting from the given node.

        Args:
            node (str): The starting node label.

        Returns:
            List[str]: A list of node labels in the order they were visited.
        """
        pass

    def dfs(self, node: str):
        """
        Performs a depth-first search starting from the given node.

        Args:
            node (str): The starting node label.

        Returns:
            List[Tuple[str, str]]: A list of edges (as tuples) in the DFS tree.
        """
        pass

    def is_tree(self):
        """
        Checks whether the graph is a tree.

        Returns:
            bool: True if the graph is connected and acyclic (i.e. a tree), False otherwise.
        """
        pass

    def print_graph(self):
        """
        Prints the graph's adjacency list representation to standard output.
        """
        pass
