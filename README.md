# Metaheuristic optimization
Discrete/Continuous optimization, Unimodal/Mutimodal problems, Python 
---

# Preamble :
---

The repo is split into two part : 
- Part 1 : Travelling Saleman problem (TSP). It is to find the shortest path, so man can visit all cities without visiting the same twice.  
- Part 2 : classical unimodal and multimodal functions shifted with a biais 

Requirements : 
- satsp
- pygmo2
- numpy
- matplotlib

# Part 1 : Discrete problem
---
In this part, we use the "satsp" package (version 0.9) to solve the TSP problem.

- Algorithm : 
There are a couple of algorithms and implementations out there for discrete optimization. **Simulated annealing** is one of the straightforward  algorithm to solve this kind of the "blob" enigma. Thanks to the simplicity of the algorithm and its implementation, a compromise between the time calculation and the performance can be satisfied. Indeed, a good result (low fitness) can be reached out with a short calculation time. Finally, the algorithm was found to be very stable and consistent for each run.  

- Requirements : install the package by the command :

```
pip install satsp
```
- Set of cities : we will investigate Djibouti (38 cities) and Qatar (192 cities)

- Benchmark : for a dimension of 38, the best path was obtained after 
