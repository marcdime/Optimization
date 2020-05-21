
# Part 2 : Shifted Functions

In this part, we will define 6 classes corresponding to 6 shifted functions we want to study. Among them, three (unimodal functions) have only global minumums  and the remainders (multimodal function) have both local and global minimum. All attributes of each class are found in the code. The main file define functions that we call to solve the problemns and visualize the results. 

- Algorithm : 
There are several algorithms for continuous optimization such as Particle Swarm Optimization, Differential Evolution, Bee colony, etc... even algorithms mostly dedicated to the discrete problems like Simulated Annealing (SA), Genetic Algorithm. Cosidering the latters, it turns out that the continous problems reveal difficulty to be efficiently solved, especially high-dimension problems and presence of local munimuns, due to bounding limits and trapping (many parameters to control exluding population, number of generation: probability of mutation, cross, cooling ....). In this part, we first try to solve the functions thanks to a set of avaliable algorithms with a same parameters. On the basis of their performance in term of convergence, then we decide to take the best algorithm to solve the problem. Two vector dimensions for each function were explored d = 50 and d = 500.    

- Install the package "pygmo" (version 2.16.0) by the command :

```
pip install pygmo
```
- Set of datasets : The  are defined   

- Parameters : the mainsteam parameters of simulated annealing are temperatures and cooling rate (alpha). Here we tune the number of epochs which is a stopping criteria or a running time, and it is somehow equivalent to given temperatures. The "best" resutls are shown after a couple of runs.     

- Benchmark : 
   - For a dimension of 38, the best path (lowest distance) was obtained after about 23 epochs with a cooling rate of 0.2 and number of epoch iterations (epoch_length) = 100. Total time of calculation = 0.58s (over 50 epochs).
   
![Convergence curves](ImgRes/TSP_Djbouti.png)

![Djibouti path](ImgRes/TSP_Djbouti_path.png)
   
   - For a dimension of 194, the best path (lowest distance) was obtained after about 100 epochs with a cooling rate of 0.4 and number of epoch iterations (epoch_length) = 500. Total time of calculation = 21.1s (over 200 epochs).
   
![Convergence curves](ImgRes/TSP_Qatar.png)

![Djibouti path](ImgRes/TSP_Qatar_path.png)

   - The solution vectors can be found in the notebook . (*Best TSP tour*) 
