#ifndef GRAPH_DFS_HPP
#define GRAPH_DFS_HPP

#include "graph_algorithm.hpp"
#include "graph.hpp"

class GraphDFS : public GraphAlgorithm {
public:
    std::vector<std::string> execute(Graph& graph, const std::string& start) override;

private:
    void dfsHelper(Graph& graph, const std::string& node, 
                   std::unordered_set<std::string>& visited, 
                   std::vector<std::string>& result);
};

#endif // GRAPH_DFS_H
