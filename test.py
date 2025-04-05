from graph_library import GraphLibrary

# Create a graph
graph = GraphLibrary()
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("A", "C")

# Run DFS
dfs_result = graph.run_dfs("A")
print("DFS Result:", dfs_result)

# Run SCC (Note: Implement SCC logic in C++)
scc_result = graph.run_scc("A")
print("SCC Result:", scc_result)

# Run Shortest Path
shortest_path = graph.run_shortest_path("A")
print("Shortest Path:", shortest_path)
