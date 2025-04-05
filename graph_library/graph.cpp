#include "graph.hpp"

void Graph::addEdge(const std::string& u, const std::string& v) {
    adjList[u].push_back(v);
}

std::vector<std::string> Graph::getNeighbors(const std::string& node) const {
    auto it = adjList.find(node);
    if (it != adjList.end()) {
        return it->second;
    }
    return {};
}
