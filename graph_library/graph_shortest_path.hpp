#ifndef GRAPH_SHORTEST_PATH_HPP
#define GRAPH_SHORTEST_PATH_HPP

#include "graph_algorithm.hpp"
#include "graph.hpp"

class GraphShortestPath : public GraphAlgorithm {
public:
    std::vector<std::string> execute(Graph& graph, const std::string& start) override;
};

#endif // GRAPH_SHORTEST_PATH_H
