## This is a python wrapper for c++ boost lib
syntax is in NetworkX style 

## Setup
run ```setup.sh```
- what it does:
  - Install python nanobind lib
  - Install c++ boost lib
  - Install locally built booty_boost lib
- Exising probelm:
  - there might be system path issue with MacOS

## How to use
Simply try any graph algorithm in the project root dir:
- add header ```import booty_boost``` 
- use NetworkX API
(for now we only implemented dfs)