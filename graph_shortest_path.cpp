#include "graph_shortest_path.hpp"
#include "graph.hpp"
#include <queue>
#include <unordered_map>

std::vector<std::string> GraphShortestPath::execute(Graph& graph, const std::string& start) {
    std::unordered_map<std::string, int> dist;
    std::unordered_map<std::string, std::string> prev;
    std::queue<std::string> q;

    dist[start] = 0;
    q.push(start);

    while (!q.empty()) {
        std::string node = q.front();
        q.pop();

        for (const auto& neighbor : graph.getNeighbors(node)) {
            if (dist.find(neighbor) == dist.end()) {
                dist[neighbor] = dist[node] + 1;
                prev[neighbor] = node;
                q.push(neighbor);
            }
        }
    }

    std::vector<std::string> path;
    for (std::string at = start; at != ""; at = prev[at]) {
        path.push_back(at);
    }

    std::reverse(path.begin(), path.end());
    return path;
}
