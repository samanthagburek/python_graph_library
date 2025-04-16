import unittest
import booty_boost as bb
import networkx as nx   # networkX shouldn't be parcled into the wheel when we release this or build CD
from networkx.algorithms.traversal import dfs_edges


# used to test our implememntation only
class TestBFSGraph(unittest.TestCase):

    def test_bfs(self):
        G = bb.Graph()
        G.add_edge("A", "B")
        G.add_edge("A", "C")
        G.add_edge("B", "D")
        G.add_edge("C", "E")

        res = G.bfs("A")    # ['A', 'B', 'C', 'D', 'E']
        assert isinstance(res, list)
        assert set(res) == {"A", "B", "C", "D", "E"}
        assert res[-1] == "E"
        assert res[0] == "A"

    def test_dfs(self):
        G = bb.Graph()
        G.add_edge("A", "B")
        G.add_edge("A", "C")
        G.add_edge("B", "D")
        G.add_edge("C", "E")

        G_nx = nx.Graph()
        G_nx.add_edges_from([
            ("A", "B"),
            ("A", "C"),
            ("B", "D"),
            ("C", "E"),
        ])

        res = G.dfs("A")   # should be   [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'E')]
        assert isinstance(res, list)
        assert res == list(dfs_edges(G_nx,"A"))
if __name__ == "__main__":
    unittest.main()
