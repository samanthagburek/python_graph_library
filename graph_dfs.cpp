#include "graph_dfs.hpp"
#include "graph.hpp"
#include <unordered_set>

std::vector<std::string> GraphDFS::execute(Graph& graph, const std::string& start) {
    std::unordered_set<std::string> visited;
    std::vector<std::string> result;
    dfsHelper(graph, start, visited, result);
    return result;
}

void GraphDFS::dfsHelper(Graph& graph, const std::string& node, 
                          std::unordered_set<std::string>& visited, 
                          std::vector<std::string>& result) {
    visited.insert(node);
    result.push_back(node);
    for (const auto& neighbor : graph.getNeighbors(node)) {
        if (visited.find(neighbor) == visited.end()) {
            dfsHelper(graph, neighbor, visited, result);
        }
    }
}
