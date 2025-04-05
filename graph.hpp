#ifndef GRAPH_HPP
#define GRAPH_HPP

#include <string>
#include <unordered_map>
#include <vector>

class Graph {
public:
    void addEdge(const std::string& u, const std::string& v);
    std::vector<std::string> getNeighbors(const std::string& node) const;

private:
    std::unordered_map<std::string, std::vector<std::string>> adjList;
};

#endif // GRAPH_HPP
