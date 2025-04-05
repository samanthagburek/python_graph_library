#include "Graph.hpp"

#include <boost/graph/adjacency_list.hpp>
#include <unordered_map>
#include <queue>
#include <vector>
#include <string>

namespace booty {

using BoostGraph = boost::adjacency_list<boost::vecS, boost::vecS, boost::undirectedS>;
using Vertex = boost::graph_traits<BoostGraph>::vertex_descriptor;

class Graph::GraphImpl {
public:
    BoostGraph graph;
    std::unordered_map<std::string, Vertex> vertexMap;
    std::unordered_map<Vertex, std::string> labelMap;
};

Graph::Graph() : impl(new GraphImpl) {}

Graph::~Graph() { delete impl; }

void Graph::add_node(const std::string& label) {
    if (impl->vertexMap.find(label) == impl->vertexMap.end()) {
        Vertex v = boost::add_vertex(impl->graph);
        impl->vertexMap[label] = v;
        impl->labelMap[v] = label;
    }
}

void Graph::add_edge(const std::string& from, const std::string& to) {
    add_node(from);
    add_node(to);
    boost::add_edge(impl->vertexMap[from], impl->vertexMap[to], impl->graph);
}

std::vector<std::string> Graph::bfs(const std::string& startLabel) {
    std::vector<std::string> result;

    if (impl->vertexMap.find(startLabel) == impl->vertexMap.end())
        return result;

    std::vector<bool> visited(boost::num_vertices(impl->graph), false);
    std::queue<Vertex> q;
    Vertex start = impl->vertexMap[startLabel];
    q.push(start);
    visited[start] = true;

    while (!q.empty()) {
        Vertex v = q.front(); q.pop();
        result.push_back(impl->labelMap[v]);

        for (auto edge : boost::make_iterator_range(boost::out_edges(v, impl->graph))) {
            Vertex neighbor = boost::target(edge, impl->graph);
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }

    return result;
}

} // namespace booty
