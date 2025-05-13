import os
import unittest
import booty_boost as bb
from opensource_cpp_base.ninja_manifest import NinjaManifest


class TestIntegration(unittest.TestCase):

    def _run_test_case(self, project_dir: str, chain_tests: list[tuple[str, str]]):
        print(f"\n\n\nTest: {project_dir}")
        ninja = NinjaManifest(project_dir)
        graph = bb.Graph()

        # Get all targets (direct and transitive dependencies)
        all_targets = set()
        for target in ninja.get_all_dependencies():  # Assuming this method gives all top-level targets
            all_targets.add(target)
            all_targets.update(ninja.deps(target))  # Add direct dependencies
            all_targets.update(ninja.transitive_deps(target))  # Add transitive dependencies

        # Add nodes to the graph
        for target in all_targets:
            graph.add_node(target)
            for dep in ninja.deps(target):
                graph.add_edge(target, dep)

        # Direct Dependency Test
        for target in all_targets:
            with self.subTest(target=target, case=project_dir):
                ninja_deps = set(ninja.deps(target))
                graph_deps = set()
                bfs = graph.bfs(target)
                if bfs:
                    for node in bfs[1:]:
                        if node in ninja_deps:
                            graph_deps.add(node)
                self.assertEqual(ninja_deps, graph_deps, f"[Direct] Difference at {target}")

        # Transitive Dependency Test
        for target in all_targets:
            with self.subTest(target=target, case=project_dir):
                ninja_trans = set(ninja.transitive_deps(target))
                graph_trans = set(graph.bfs(target))
                graph_trans.discard(target)
                self.assertEqual(ninja_trans, graph_trans, f"[Transitive] Difference at {target}")

        # Dependency Chain Test (Allow Differences but Record)
        for source, destination in chain_tests:
            with self.subTest(chain=(source, destination), case=project_dir):
                try:
                    ninja_chain = ninja.dependency_chain(source, destination)
                except Exception as e:
                    ninja_chain = []
                    print(f"NinjaManifest error: {e}")
                graph_chain = self._find_chain(graph, source, destination)

                self.assertTrue(graph_chain, f"[Chain] Cannot find path from {source} → {destination}")
                self.assertEqual(ninja_chain[0], graph_chain[0],
                                 f"[Chain] Start point differs: {ninja_chain[0]} ≠ {graph_chain[0]}")
                self.assertEqual(ninja_chain[-1], graph_chain[-1],
                                 f"[Chain] End point differs: {ninja_chain[-1]} ≠ {graph_chain[-1]}")
                self.assertIn(destination, graph_chain, f"[Chain] {destination} not in Graph path")

                # Record differences
                if ninja_chain != graph_chain:
                    print(f"Chain structure differs: {source} → {destination}")
                    print(f"  NinjaManifest: {ninja_chain}")
                    print(f"  BootyBoost   : {graph_chain}")
                    log_dir = os.path.dirname(os.path.abspath(__file__))
                    os.makedirs(log_dir, exist_ok=True)
                    log_file = os.path.join(log_dir, "chain_diff_log.txt")
                    with open(log_file, "a") as f:
                        f.write(f"{project_dir} | {source} → {destination}\n")
                        f.write(f"  NinjaManifest: {ninja_chain}\n")
                        f.write(f"  BootyBoost   : {graph_chain}\n\n")

    def _find_chain(self, graph, source, destination):
        """Find a valid path from source to destination in booty_boost.Graph"""
        dfs_edges = graph.dfs(source)  # Returns List[Tuple[u, v]]

        # Build adjacency list
        adj = {}
        for u, v in dfs_edges:
            if u not in adj:
                adj[u] = []
            adj[u].append(v)

        # Normal DFS to build path
        stack = [(source, [source])]
        visited = set()
        while stack:
            node, path = stack.pop()
            if node == destination:
                return path
            if node in visited:
                continue
            visited.add(node)
            for neighbor in adj.get(node, []):
                if neighbor not in path:
                    stack.append((neighbor, path + [neighbor]))
        return []

    def test_case1(self):
        case_dir = os.path.abspath("test_data/case1")
        chains = [("hello", "hello.cc")]
        self._run_test_case(case_dir, chains)

    def test_case2(self):
        case_dir = os.path.abspath("test_data/case2")
        chains = [
            ("hello", "util.cc"),
            ("hello", "hello.cc"),
            ("app", "math.cc"),
        ]
        self._run_test_case(case_dir, chains)


