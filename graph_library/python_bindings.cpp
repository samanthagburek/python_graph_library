#include <nanobind/nanobind.hpp>
#include "graph.hpp"
#include "graph_dfs.hpp"
#include "graph_scc.hpp"
#include "graph_shortest_path.hpp"

namespace nb = nanobind;

NB_MODULE(graph_backend, m) {
    nb::class_<Graph>(m, "Graph")
        .def("add_edge", &Graph::addEdge)
        .def("get_neighbors", &Graph::getNeighbors);

    nb::class_<GraphDFS, GraphAlgorithm>(m, "GraphDFS")
        .def("execute", &GraphDFS::execute);

    nb::class_<GraphSCC, GraphAlgorithm>(m, "GraphSCC")
        .def("execute", &GraphSCC::execute);

    nb::class_<GraphShortestPath, GraphAlgorithm>(m, "GraphShortestPath")
        .def("execute", &GraphShortestPath::execute);
}
