import unittest
import booty_boost

class TestBFSGraph(unittest.TestCase):

    def setUp(self):
        self.g = Graph()
        for node in ["A", "B", "C", "D", "E"]:
            self.g.add_node(node)
        
        # Add edges with some cycles and a path
        self.g.add_edge("A", "B")
        self.g.add_edge("B", "C")
        self.g.add_edge("C", "A")  # forms a cycle A -> B -> C -> A
        self.g.add_edge("C", "D")
        self.g.add_edge("D", "E")

    def test_bfs(self):
        bfs_order = self.g.create_bfs("A")
        # Order can vary, but all reachable nodes should be present
        expected_nodes = set(["A", "B", "C", "D", "E"])
        self.assertEqual(set(bfs_order), expected_nodes)
        self.assertEqual(bfs_order[0], "A")  # BFS should start at A

    def test_scc(self):
        scc = self.g.compute_scc()
        # A, B, C should be in the same strongly connected component
        group_abc = scc["A"]
        self.assertEqual(scc["B"], group_abc)
        self.assertEqual(scc["C"], group_abc)
        # D and E should be in different components
        self.assertNotEqual(scc["D"], group_abc)
        self.assertNotEqual(scc["E"], group_abc)

    def test_shortest_path(self):
        path = self.g.shortest_path("A", "E")
        self.assertEqual(path, ["A", "B", "C", "D", "E"])

        no_path = self.g.shortest_path("E", "A")
        self.assertEqual(no_path, [])  # Directed graph, no path back

if __name__ == "__main__":
    unittest.main()
