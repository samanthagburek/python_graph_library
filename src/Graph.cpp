#include "Graph.hpp"

#include <boost/graph/breadth_first_search.hpp>
#include <boost/graph/depth_first_search.hpp>
#include <boost/graph/adjacency_list.hpp>
#include <unordered_map>
#include <queue>
#include <vector>
#include <string>
#include <tuple>
#include <iostream>

namespace booty {

using BoostGraph = boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS>;
using Vertex = boost::graph_traits<BoostGraph>::vertex_descriptor;

class Graph::GraphImpl {
public:
    BoostGraph graph;
    std::unordered_map<std::string, Vertex> vertexMap;
    std::unordered_map<Vertex, std::string> labelMap;
};

Graph::Graph() : impl(new GraphImpl) {}

Graph::~Graph() { delete impl; }

//customized struct inherits from default. Customized event handle. Used only once
struct BfsVisitor : public boost::default_bfs_visitor {
    std::vector<std::string>& result;
    std::unordered_map<Vertex, std::string>& labelMap;

    BfsVisitor(std::vector<std::string>& r, std::unordered_map<Vertex, std::string>& l)
        : result(r), labelMap(l) {}

    void discover_vertex(Vertex v, const BoostGraph&) {
        result.push_back(labelMap[v]);
    }
};

struct DfsVisitor : public boost::default_dfs_visitor {
    std::vector<std::tuple<std::string, std::string>>& result;
    std::unordered_map<Vertex, std::string>& labelMap;

    DfsVisitor(std::vector<std::tuple<std::string, std::string>>& r, std::unordered_map<Vertex, std::string>& l)
        : result(r), labelMap(l) {}

    void tree_edge(boost::graph_traits<BoostGraph>::edge_descriptor e, const BoostGraph& g) {
        Vertex u = boost::source(e, g);
        Vertex v = boost::target(e, g);
        result.emplace_back(labelMap[u], labelMap[v]);
    }
};

bool Graph::add_node(const std::string& label) {
    if (impl->vertexMap.find(label) == impl->vertexMap.end()) {
        Vertex v = boost::add_vertex(impl->graph);
        impl->vertexMap[label] = v;
        impl->labelMap[v] = label;
        return true;
    }
    return false;
}

bool Graph::add_edge(const std::string& from, const std::string& to) {
    add_node(from);
    add_node(to);
    // std::pair<boost::edge_descriptor, bool> is boost::add_edge return type, no repeated add issue.
    auto result = boost::add_edge(impl->vertexMap[from], impl->vertexMap[to], impl->graph);
    return result.second; // true if the edge was added, false if it already existed
}


std::vector<std::string> Graph::bfs(const std::string& startLabel) {
    std::vector<std::string> result;

    if (impl->vertexMap.find(startLabel) == impl->vertexMap.end())
        return result;  //empty

    std::vector<boost::default_color_type> color(boost::num_vertices(impl->graph));
    Vertex start = impl->vertexMap[startLabel];

    BfsVisitor vis(result, impl->labelMap);
    /**ok this is kinda ugly
        must have a specified color map (state indication)
        each vertex is mapped to an ind pos in the color map (call getter) for iterator
    **/
    boost::breadth_first_search
    (
        impl->graph, start,
        boost::visitor(vis).color_map(boost::make_iterator_property_map(color.begin(), boost::get(boost::vertex_index, impl->graph)))
    );

    return result;
}

std::vector<std::tuple<std::string, std::string>> Graph::dfs(const std::string& startLabel) {
    std::vector<std::tuple<std::string, std::string>> result;

    if (impl->vertexMap.find(startLabel) == impl->vertexMap.end())
        return result;  //empty!

    std::vector<boost::default_color_type> color(boost::num_vertices(impl->graph));
    Vertex start = impl->vertexMap[startLabel];

    DfsVisitor vis(result, impl->labelMap);
    boost::depth_first_visit(impl->graph, start, vis, boost::make_iterator_property_map(color.begin(), boost::get(boost::vertex_index, impl->graph)));

    return result;
}

bool Graph::is_tree(){ //I should set this as constant method but, nay.
    std::size_t numV = boost::num_vertices(impl->graph);
    std::size_t numE = boost::num_edges(impl->graph);
    if (numE != numV - 1){return false;}    //no further check needed. Capture cyclical/disconnect.
    if (numV==1){return true;}  //a singular node considered true
//    std::string startLabel = impl->vertexMap.begin()->first;    //for undirected, using any arbitrary node as starting point
       std::vector<std::string> roots;
    for (const auto& pair : impl->vertexMap) {
        auto v = pair.second;
        if (boost::in_degree(v, impl->graph) == 0) {
            roots.push_back(pair.first);
        }
    }
    if (roots.size()!=1)return false;   //strictly one root

    std::vector<std::string> reachable = bfs(roots[0]); //use bfs to scan
    return reachable.size() == numV;
}

// Iterates over out-edges to simulate adjacency list
//will need to be changed if use directed graphs too 
void Graph::print_graph() const {
    for (const auto& pair : impl->vertexMap) {
        const std::string& label = pair.first;
        Vertex v = pair.second;
        std::cout << label << " -> ";
        for (auto edge : boost::make_iterator_range(boost::out_edges(v, impl->graph))) {
            Vertex neighbor = boost::target(edge, impl->graph);
            std::cout << impl->labelMap[neighbor] << " ";
        }
        std::cout << std::endl;
    }
}


} // namespace booty
