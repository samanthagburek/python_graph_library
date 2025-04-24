## This is a python wrapper for c++ boost lib
syntax is in NetworkX style 

## Setup
```bash
pip install .

This will build the booty_boost library, which can then be imported.

```
## Interface

Currently the library consists only of an interface definition and mocked tests 
for it. In the future, an implementation using the CPP boost library will be added.

### methods
This interface currently supports a few methods:
- add_node
- add_edge
- bfs
- dfs
- is_tree
- print_graph

More information on them can be seen in the docstrings.


## Tests
There are currently 2 test files in the `tests/` directory:
- a sanity check that just probes the class for its methods
- a unittest class that tests most of the methods in the class

Currently, they are both supported by a `MagicMock` implementation.
