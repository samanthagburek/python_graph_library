cmake_minimum_required(VERSION 3.10)
project(GraphLibrary)

set(CMAKE_CXX_STANDARD 17)

# Nanobind configuration
find_package(Nanobind REQUIRED)

add_library(graph_backend SHARED
    graph.cpp
    graph_dfs.cpp
    graph_scc.cpp
    graph_shortest_path.cpp
    python_bindings.cpp
)

target_link_libraries(graph_backend PRIVATE nanobind::nanobind)

