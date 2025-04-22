#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/vector.h>
#include <nanobind/stl/tuple.h>
#include "Graph.hpp"

namespace nb = nanobind;
using namespace nb::literals;

NB_MODULE(_booty_boost, m) {
    nb::class_<booty::Graph>(m, "Graph")
        .def(nb::init<>())
        .def("add_node", &booty::Graph::add_node)
        .def("add_edge", &booty::Graph::add_edge)
        .def("bfs", &booty::Graph::bfs)
        .def("dfs", &booty::Graph::dfs)
        .def("is_tree", &booty::Graph::is_tree);
}
