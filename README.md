## This is a python wrapper for c++ boost lib
syntax is in NetworkX style 

## Setup
```bash
pip install .
```

boost can be found by cmakelist directly.
(this is really nice because the lib is huge.)
**the rest runs out of box yay!**


## How to use
Simply try any graph algorithm in the project root dir:
- add header ```import booty_boost``` 
- use NetworkX API
(for now we only implemented dfs and bfs)

## Still not sure?
- check [unittest.py](./unittests.py)
- you can create a .py file in the project directory (outside /src)
  - in the .py file, have this line:
  - ```python
    import booty_boost
    ```
    Then you can create your own graph, for now we only have ``add_edge(from, to)`` method
  - and you can run dfs and bfs on the graph you just created!

## Regarding homework requirements
  - We are waiting for prof Yotov's feedback on homework2, interface.
  - so far the closest thing we have to an interface is the [Graph.hpp file](src/Graph.hpp)
  - Depends on what prof Yotov recommends, we might write an Abstract Base Class object in python as the interface.

## Hat-tip:
- this project is inspired by a [tutorial on setting up cpp backend for python](https://nanobind.readthedocs.io/en/latest/packaging.html)