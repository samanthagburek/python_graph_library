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
    std::vector<std::string> bfs(const std::string& startLabel); // return type bound to list of strings in python
    std::vector<std::tuple<std::string, std::string>> dfs(const std::string& startLabel); //return type bound to list of tuples of strings in python
    bool is_tree(); //implementation 
private:
    class GraphImpl;
    GraphImpl* impl;
};

} // namespace booty

#endif // GRAPH_HPP
