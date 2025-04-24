import unittest
from unittest.mock import MagicMock
import booty_boost as bb
import networkx as nx  # networkX shouldn't be parcled into the wheel when we release this or build CD
from networkx.algorithms.traversal import dfs_edges


# used to test our interface only, all implementation is mocked
class TestBFSGraphInterface(unittest.TestCase):
    def test_add_edge(self):
        G = MagicMock(bb.BaseGraph)
        G.add_edge.return_value = True

        added = G.add_edge("A", "B")
        assert added, "Expected edge A -> B to be newly added"

    def test_bfs(self):
        G = MagicMock(bb.BaseGraph)
        G.bfs.return_value = ["A", "B", "C", "D", "E"]

        G.add_edge("A", "B")
        G.add_edge("A", "C")
        G.add_edge("B", "D")
        G.add_edge("C", "E")

        res = G.bfs("A")  # ['A', 'B', 'C', 'D', 'E']
        assert isinstance(res, list)
        assert set(res) == {"A", "B", "C", "D", "E"}
        assert res[-1] == "E"
        assert res[0] == "A"

    def test_dfs(self):
        G = MagicMock(bb.BaseGraph)
        G.dfs.return_value = [("A", "B"), ("B", "D"), ("A", "C"), ("C", "E")]

        G.add_edge("A", "B")
        G.add_edge("A", "C")
        G.add_edge("B", "D")
        G.add_edge("C", "E")

        G_nx = nx.Graph()
        G_nx.add_edges_from(
            [
                ("A", "B"),
                ("A", "C"),
                ("B", "D"),
                ("C", "E"),
            ]
        )

        res = G.dfs("A")  # should be   [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'E')]
        assert isinstance(res, list)
        assert res == list(dfs_edges(G_nx, "A"))

    # is_tree method depends on bfs and edge counting
    def test_is_tree(self):
        G = MagicMock(bb.BaseGraph)
        G.is_tree.return_value = True

        G.add_edge("A", "B")
        G.add_edge("A", "C")
        assert G.is_tree() == True
        G.add_edge("B", "C")  # triangular cyclical assoc A-B-C

        G.is_tree.return_value = False

        assert G.is_tree() == False


if __name__ == "__main__":
    unittest.main()
