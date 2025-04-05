import unittest
import booty_boost as gg

class TestBFSGraph(unittest.TestCase):

    def test_dfs_traversal():
        graph = gg.Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")
        graph.add_edge("C", "D")

        # pass in graph and source
        result = gg.GraphDFS(graph, "A")

        assert isinstance(result, list)
        assert set(result) == {"A", "B", "C", "D"}
        assert result[0] == "A"

    def test_strongly_connected_components():
        graph = gg.Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")
        graph.add_edge("C", "D")

        # only need graph
        result = gg.GraphSCC(graph)

        assert isinstance(result, list)
        assert any(set(comp) == {"A", "B", "C"} for comp in result)

    def test_shortest_path():
        graph = gg.Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")
        graph.add_edge("C", "D")

        # pass in start and target
        result = gg.GraphShortestPath(graph, "A", "D")

        assert isinstance(result, dict)
        assert result["A"] == 0
        assert result["B"] == 1
        assert result["C"] == 1
        assert result["D"] == 2

if __name__ == "__main__":
    unittest.main()
