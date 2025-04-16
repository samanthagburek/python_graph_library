#ifndef GRAPH_HPP
#define GRAPH_HPP

#include <string>
#include <vector>

namespace booty {

class Graph {
public:
    Graph();
    ~Graph();

    void add_node(const std::string& label);
    void add_edge(const std::string& from, const std::string& to);
    std::vector<std::string> bfs(const std::string& startLabel); // RETURN vector instead of print
    std::vector<std::tuple<std::string, std::string>> dfs(const std::string& startLabel);
private:
    class GraphImpl;
    GraphImpl* impl;
};

} // namespace booty

#endif // GRAPH_HPP
