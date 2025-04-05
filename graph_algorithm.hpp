#ifndef GRAPH_ALGORITHM_HPP
#define GRAPH_ALGORITHM_HPP

#include <string>
#include <vector>

class Graph;  // Forward declaration of the Graph class

class GraphAlgorithm {
public:
    virtual std::vector<std::string> execute(Graph& graph, const std::string& start) = 0;
    virtual ~GraphAlgorithm() = default;
};

#endif // GRAPH_ALGORITHM_HPP
