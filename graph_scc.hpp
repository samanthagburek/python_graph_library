#ifndef GRAPH_SCC_HPP
#define GRAPH_SCC_HPP

#include "graph_algorithm.hpp"
#include "graph.hpp"
#include <unordered_set>
#include <vector>

class GraphSCC : public GraphAlgorithm {
public:
    std::vector<std::unordered_set<std::string>> execute(Graph& graph, const std::string& start) override;
};

#endif // GRAPH_SCC_HPP
