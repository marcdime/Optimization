
# Part 2 : Shifted Functions

In this part, we will define 6 classes corresponding to 6 shifted functions we want to study. Among them, three (unimodal functions) have only global minumums  and the remainders (multimodal function) have both local and global minimums. All attributes of each class are found in the code. The main file define functions that we call to solve the problemns and visualize the results. 

- Algorithm : 
There are several algorithms for continuous optimization such as Particle Swarm Optimization, Differential Evolution, Bee colony, etc... even algorithms mostly dedicated to the discrete problems like Simulated Annealing (SA), Genetic Algorithm. Cosidering the latters, it turns out that the continous problems reveal difficulty to be efficiently solved, especially high-dimension problems and presence of local munimuns, due to bounding limits and trapping (many parameters to control exluding population, number of generation: probability of mutation, cross, cooling ....). In this part, we first try to solve the functions thanks to a set of avaliable algorithms with a same parameters. On the basis of their performance in term of convergence, then we decide to take the best algorithm to solve the problem. Two vector dimensions for each function were explored d = 50 and d = 500.    

- Install the package "pygmo" (version 2.16.0) by the command :

```
pip install pygmo
```
Copy all .py files in a folder, import files and run as shown in the notebook.

- Functions and vectors x, shift values : 
Functions investigated are conventional functions plus a shift (or biais) which is given in a separated file named shift.py. The values of the vectors x for optimization are also found in this file.  

- Parameters : 
Classical parameters such as number of individuals in the populaton, number of generations are taken as inputs in each running function. Additional parameters are also givent as inputs for particular case, i. e. self confidence, inertia, swarm confidence when running PSO. The parameters are modified to check the influence of these parameters for the performance and the time calculation.

Note that the stopping criterion is the number of function evaluations (except for Self-adaptive Differential Evolution algorithm, that is function tolerance) and the convergence shown is the best run after a number of *epoch_runs*   
   

- Benchmark : 
All the results (fitness, calculation time, convergence, function evaluations, etc....) can be found in the notebook. 
