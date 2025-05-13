## This is a python wrapper for c++ boost lib
syntax is in NetworkX style 

## Setup
```bash
uv pip install .


boost can be found by cmakelist directly.
(this is really nice because the lib is huge.)
**the rest runs out of box yay!**

This will build the booty_boost library, which can then be imported.

```
## Interface and implementation

Currently the library consists of an interface definition and an implementation
for it using the CPP boost library.

### methods
This interface currently supports a few methods:
- add_node
- add_edge
- bfs
- dfs
- is_tree
- print_graph

More information on them can be seen in the docstrings in the [interface](src/booty_boost/interface.py).

## How to use
Simply try any graph algorithm in the project root dir:
- add header ```import booty_boost as bb``` 
- use NetworkX-like API, as our interface describes

## Still not sure?
- check [test_graph.py](./test_graph.py) for a usage example

## Tests
There are currently 2 test files in the `tests/` directory:
- a sanity check that just probes the class for its methods
- a unittest class that tests most of the methods in the class

## Update on Integration
This repo has added a submodule from a [c++ Ninja graph library](https://github.com/seongjaeny/opensource_cpp_base/tree/integration) from their "integration" branch.
We are not sure what to do with it yet, but note that now if you want to clone from our [integration branch](https://github.com/samanthagburek/python_graph_library/tree/integration),
you would then further need to:
```bash
git submodule init
git submodule update
```
Note: for use with Ninja graph, ``Integration`` branch implements bi-directional graph (other branches are undirected) which might lead to broken bfs/dfs/graph iteration.
