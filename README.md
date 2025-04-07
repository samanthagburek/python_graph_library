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
(for now we only implemented dfs)

## Hat-tip:
- this project is inspired by a [tutorial on setting up cpp backend for python](https://nanobind.readthedocs.io/en/latest/packaging.html)