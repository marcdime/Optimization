
# Part 2 : Shifted Functions

In this part, we will define 6 classes corresponding to 6 shifted functions we want to study. Among them, three (unimodal functions) have only global minimums and the remainders (multimodal functions) have both local and global minimums. The core file (main.py) defines functions that we call to solve the problemns and visualize the results. 

- Algorithm : there are several algorithms for continuous optimization such as Particle Swarm Optimization (PSO), Differential Evolution, Bee colony, etc... even algorithms mostly dedicated to the discrete problems such as Simulated Annealing (SA), Genetic Algorithm. For the latters, it turns out that the continuous optimization appears to be not efficiently solved, especially for high-dimension problems and presence of local munimums, due to bounding limits, trapping and several "hazard" parameters exluding population and number of generations,  to control the convergence (probability of mutation, cross, cooling rate, etc....). In this part, we first try to solve the functions thanks to a set of avalaible algorithms with same parameters, for instance dimension of 10. On the basis of their performance in term of convergence, we then decide to take the best algorithm to solve the problem by tuning its own parameters. Two vector dimensions for each function are explored D = 50 and D = 500.    

- Install the package "pygmo" (version 2.16.0) by the command :

```
pip install pygmo
```
Copy all .py files in a folder, import files and run as shown in the notebook.

- Functions and vectors x, shift values : functions investigated are conventional functions plus a shift (or biais) which is given in a separated file named shift.py. The values of the vectors x for optimization are also found in this file.  

- Parameters : classical parameters such as number of individuals in a populaton, number of generations are taken as inputs in each running function. Additional parameters are also given as inputs for particular case, for instance self confidence, inertia, swarm confidence when running PSO. The parameters are modified to check the influence of these parameters for the performance and the time calculation.

Note that the stopping criterion is the number of function evaluations (except for Self-adaptive Differential Evolution algorithm, that is function tolerance) and the convergence curves come from the best run after a number of *epoch_runs*   
   

- Benchmark : all the results (fitness, calculation time, convergence, function evaluations, etc....) are shown in the notebook. By this we can easily assess the performance of an algorithm in term of parameter tuning and compare the performance between algorithms.
