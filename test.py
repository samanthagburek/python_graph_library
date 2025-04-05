import booty_boost as bb

G = bb.Graph()
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "D")
G.add_edge("C", "E")

print(G.bfs("A"))  # ['A', 'B', 'C', 'D', 'E']
