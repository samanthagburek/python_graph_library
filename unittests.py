import unittest
import booty_boost as bb

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

if __name__ == "__main__":
    unittest.main()
