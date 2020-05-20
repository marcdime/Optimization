# Part 1 : Travelling Saleman Problem

In this part, we use "satsp" package (version 0.9) to solve the TSP problem.

- Algorithm : 
There are a couple of algorithms and implementations out there for discrete optimization. **Simulated annealing** is one of the straightforward  algorithm to solve this kind of the "blob" enigma. Thanks to the simplicity of the algorithm and its implementation, a compromise between the time calculation and the performance can be satisfied. Indeed, a good result (low fitness) can be reached out with a short calculation time. Finally, the algorithm was found to be very stable and consistent for each run.  

- Requirements : install the package by the command :

```
pip install satsp
```
- Set of cities : we will investigate Djibouti (38 cities) and Qatar (192 cities)
- Parameters : the mainsteam parameters of simulated annealing are temperatures and cooling rate (alpha). Here we tune the number of epochs which is a stopping criteria or a running time, which is somehow equivalent to given temperatures.   

- Benchmark : 
   - for a dimension of 38, the best path (lowest distance) was obtained after 23  epochs
