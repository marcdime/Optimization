from MetaClass import *


prob_instance = None

def viz_2dim(x_range, y_range, step, prob_instance):

	# Generate data dimesion 2
	x = np.arange((-x_range), (x_range)+step, step)
	y = np.arange((-y_range), (y_range)+step, step) 
	x,y = np.meshgrid(x,y)	
	xy = np.mgrid[(-x_range):x_range+step:step, (-y_range):y_range+step:step].reshape(2,-1).T
		
	prob = pg.problem(prob_instance)
	f = np.array([prob.fitness(i) for i in xy]).reshape(x.shape)

	# Plot the surface.
	fig = plt.figure(figsize=(14,10))
	ax = fig.gca(projection='3d')
	surf = ax.plot_surface(x, y, f, cmap=cm.coolwarm, linewidth=0, antialiased=False, alpha = 0.8)
	plt.gca().invert_zaxis()

	#Projection on (xy) plane
	cset = ax.contourf(x, y, f, zdir='z', offset=prob_instance.get_offset(), cmap=cm.coolwarm, alpha = 0.5)
	
	# Add a color bar which maps values to colors.
	fig.colorbar(surf, shrink=0.5, aspect=5)
	ax.view_init(-150, -160)
	plt.show()


def run_algos(prob_instance, generations, num_individuals_pop):  
	prob = pg.problem(prob_instance)
	algos = [pg.sade(gen=generations), pg.de(gen=generations), pg.de1220(gen=generations), 
			 pg.pso(gen=generations), pg.bee_colony(gen=generations, limit=20)]

	epoch_runs = 10
	plt.figure(figsize = (12,6))

	# Loop in the algo list
	for index,uda in enumerate(algos):
		logs = []
		# Loop and take the average of results for each algo
		for i in range(epoch_runs):
			algo = pg.algorithm(uda)
			algo.set_verbosity(1) # regulates both screen and log verbosity
			pop = pg.population(prob, num_individuals_pop)
			pop = algo.evolve(pop)
			extraction = algo.extract(type(uda))
			log = extraction.get_log()
			logs.append(log)
		   
		logs = np.array(logs)
		
		avg_logs = np.average(logs,axis = 0)
		plt.plot(avg_logs[:,0], avg_logs[:,2], label=algo.get_name())
		plt.xlabel("Generations")
		plt.ylabel("Best fitness")
		plt.legend()
	plt.show() 


def run_pso(prob_instance, epoch_runs, generations, inertia, self_confidence , swarm_confidence, num_individuals_pop):
	'''
	- inertia factor : current motion (0.4 - 1.4)
	- self_confidence :  effect of particle memory (particle best ever position) to the particle velocity (1.5 - 2.0)
	- swarm_confidence : effect of swarm infuence (best position in current swarm ). Magnitude of the force, applied to the 
						 particle’s velocity, in the direction of the best position in its neighborhood) (2.0 -2.5)
	'''
	prob = pg.problem(prob_instance)

	start_time = time.time()

	best_solution = ()

	
	for i in range(epoch_runs):

		start_time_run = time.time()

		algo = pg.algorithm(pg.pso(gen = generations, 
								   omega = inertia, 
								   eta1 = self_confidence, 
								   eta2 = swarm_confidence))
		algo.set_verbosity(1)  # to screen show
		pop = pg.population(prob, num_individuals_pop)		
		pop = algo.evolve(pop)	   
		uda = algo.extract(pg.pso)	

		elapse_run = time.time() - start_time_run	
		
		if i == 0:
			best_fitness_in_runs = pop.get_f()[pop.best_idx()]
			best_solution = (best_fitness_in_runs, pop.get_x()[pop.best_idx()])
			best_elapse_runs = elapse_run
			log = uda.get_log()
				
		if best_fitness_in_runs > pop.get_f()[pop.best_idx()]:
			best_fitness_in_runs = pop.get_f()[pop.best_idx()]
			best_solution = (best_fitness_in_runs, pop.get_x()[pop.best_idx()])
			best_elapse_runs = elapse_run
			log = uda.get_log()

	elapse = time.time() - start_time
	
	print("Problem : {} \n{}".format(prob.get_name(), prob.get_extra_info()))
	print("Best solution vector :\n {} \nBest fitness : {}".format(best_solution[1], best_solution[0]))
	print("Time of calculation of the best run : {}".format(str(timedelta(seconds=elapse_run))))
	print("Total time of calculation (over {} runs) : {}".format(epoch_runs, str(timedelta(seconds=elapse))))

	# Plot the convergence : Best fitness vs time and best fitness vs function evaluations
	x_time = np.arange(0, best_elapse_runs, best_elapse_runs/len(log))
	x_num = [row[1] for row in log]
	y = [row[2]  for row in log]

	if len(x_time) > len(y):
		x_time = x_time[:-1]
	elif len(x_time) < len(y):
		x_time.append(x_time[-1] + best_elapse_runs)

	assert(len(x_time)==len(y)), "Timing error !!! \n No worry, run again !"

	fig = plt.figure(figsize = (14,4))
	ax1 = fig.add_subplot(1,2,1)
	ax2 = fig.add_subplot(1,2,2)
	
	ax1.plot(x_time,y, color = "blue")
	ax1.set_title("Fitness vs time (best run)", fontsize=16)
	ax1.set_xlabel("Time (s)", fontsize = 14)
	ax1.set_ylabel("Best fitness", fontsize = 14)
	
	ax2.plot(x_num,y, color = "orange")
	ax2.set_title("Fitness vs Fevals (best run)",  fontsize=16)
	ax2.set_xlabel("Number of function evaluations", fontsize = 14)
	ax2.set_ylabel("Best fitness", fontsize = 14)
	plt.show()



def run_abc(prob_instance, epoch_runs, generations, limit, num_individuals_pop):
	'''
	Bee_colonny
	- limit : 
	'''
	prob = pg.problem(prob_instance)

	start_time = time.time()

	best_solution = ()

	
	for i in range(epoch_runs):	

		start_time_run = time.time()

		algo = pg.algorithm(pg.bee_colony(gen = generations, limit = limit))
		algo.set_verbosity(1)  # to screen show
		pop = pg.population(prob, num_individuals_pop)		
		pop = algo.evolve(pop)	   
		uda = algo.extract(pg.bee_colony)

		elapse_run = time.time() - start_time_run		
		
		if i == 0:
			best_fitness_in_runs = pop.get_f()[pop.best_idx()]
			best_solution = (best_fitness_in_runs, pop.get_x()[pop.best_idx()])
			best_elapse_runs = elapse_run
			log = uda.get_log()
				
		if best_fitness_in_runs > pop.get_f()[pop.best_idx()]:
			best_fitness_in_runs = pop.get_f()[pop.best_idx()]
			best_solution = (best_fitness_in_runs, pop.get_x()[pop.best_idx()])
			best_elapse_runs = elapse_run
			log = uda.get_log()

	elapse = time.time() - start_time
	
	
	print("Problem : {} \n{}".format(prob.get_name(), prob.get_extra_info()))
	print("Best solution vector :\n {} \nBest fitness : {}".format(best_solution[1], best_solution[0]))
	print("Time of calculation of the best run : {}".format(str(timedelta(seconds=elapse_run))))
	print("Total time of calculation (over {} runs) : {}".format(epoch_runs, str(timedelta(seconds=elapse))))

	# Plot the convergence : Best fitness vs time and best fitness vs function evaluations
	x_time = np.arange(0, best_elapse_runs, best_elapse_runs/len(log))
	x_num = [row[1] for row in log]
	y = [row[2]  for row in log]

	if len(x_time) > len(y):
		x_time = x_time[:-1]
	elif len(x_time) < len(y):
		x_time.append(x_time[-1] + best_elapse_runs)

	assert(len(x_time)==len(y)), "Timing error !!! \n No worry, run again !"
	
	fig = plt.figure(figsize = (14,4))
	ax1 = fig.add_subplot(1,2,1)
	ax2 = fig.add_subplot(1,2,2)
	
	ax1.plot(x_time,y, color = "blue")
	ax1.set_title("Fitness vs time", fontsize=16)
	ax1.set_xlabel("Time (s)", fontsize = 14)
	ax1.set_ylabel("Best fitness", fontsize = 14)
	
	ax2.plot(x_num,y, color = "orange")
	ax2.set_title("Fitness vs Fevals (best run)",  fontsize=16)
	ax2.set_xlabel("Number of function evaluations", fontsize = 14)
	ax2.set_ylabel("Best fitness", fontsize = 14)
	plt.show()


def run_sga(prob_instance, epoch_runs, generations, num_individuals_pop):
	'''
	Simple genetic algorithm 
	'''
	prob = pg.problem(prob_instance)

	start_time = time.time()

	best_solution = ()

	
	for i in range(epoch_runs):

		start_time_run = time.time()

		algo = pg.algorithm(pg.sga(gen = generations))
		algo.set_verbosity(1)  # to screen show
		pop = pg.population(prob, num_individuals_pop)		
		pop = algo.evolve(pop)	   
		uda = algo.extract(pg.sga)

		elapse_run = time.time() - start_time_run
		
 
		if i == 0:
			best_fitness_in_runs = pop.get_f()[pop.best_idx()]
			best_solution = (best_fitness_in_runs, pop.get_x()[pop.best_idx()])
			best_elapse_runs = elapse_run
			log = uda.get_log()
			
				
		if best_fitness_in_runs > pop.get_f()[pop.best_idx()]:
			best_fitness_in_runs = pop.get_f()[pop.best_idx()]
			best_solution = (best_fitness_in_runs, pop.get_x()[pop.best_idx()])
			best_elapse_runs = elapse_run
			log = uda.get_log()

	elapse = time.time() - start_time
	
	
	print("Problem : {} \n{}".format(prob.get_name(), prob.get_extra_info()))
	print("Best solution vector :\n {} \nBest fitness : {}".format(best_solution[1], best_solution[0]))
	print("Time of calculation of the best run : {}".format(str(timedelta(seconds=elapse_run))))
	print("Total time of calculation (over {} runs) : {}".format(epoch_runs, str(timedelta(seconds=elapse))))

	# Plot the convergence : Best fitness vs time and best fitness vs function evaluations
	x_time = np.arange(0, best_elapse_runs, best_elapse_runs/len(log))
	x_num = [row[1] for row in log]
	y = [row[2]  for row in log]

	if len(x_time) > len(y):
		x_time = x_time[:-1]
	elif len(x_time) < len(y):
		x_time.append(x_time[-1] + best_elapse_runs)

	assert(len(x_time)==len(y)), "Timing error !!! \n No worry, run again !"
	
	fig = plt.figure(figsize = (14,4))
	ax1 = fig.add_subplot(1,2,1)
	ax2 = fig.add_subplot(1,2,2)
	
	ax1.plot(x_time,y, color = "blue")
	ax1.set_title("Fitness vs time (best run)", fontsize=15)
	ax1.set_xlabel("Time (s)", fontsize = 14)
	ax1.set_ylabel("Best fitness", fontsize = 14)
	
	ax2.plot(x_num,y, color = "orange")
	ax2.set_title("Fitness vs Fevals (best run)",  fontsize=15)
	ax2.set_xlabel("Number of function evaluations", fontsize = 14)
	ax2.set_ylabel("Best fitness", fontsize = 14)
	plt.show()



def run_sade(prob_instance, epoch_runs, generations, f_tolerance, num_individuals_pop):
	'''
	Self-adaptive Differential Evolution
	- f_tolerance : stopping critera on the f tolerance
	'''
	prob = pg.problem(prob_instance)

	start_time = time.time()

	best_solution = ()

	
	for i in range(epoch_runs):

		start_time_run = time.time()

		algo = pg.algorithm(pg.sade(gen = generations, xtol = f_tolerance))
		algo.set_verbosity(1)  # to screen show
		pop = pg.population(prob, num_individuals_pop)		
		pop = algo.evolve(pop)	   
		uda = algo.extract(pg.sade)

		elapse_run = time.time() - start_time_run
		
 
		if i == 0:
			best_fitness_in_runs = pop.get_f()[pop.best_idx()]
			best_solution = (best_fitness_in_runs, pop.get_x()[pop.best_idx()])
			best_elapse_runs = elapse_run
			log = uda.get_log()
			
				
		if best_fitness_in_runs > pop.get_f()[pop.best_idx()]:
			best_fitness_in_runs = pop.get_f()[pop.best_idx()]
			best_solution = (best_fitness_in_runs, pop.get_x()[pop.best_idx()])
			best_elapse_runs = elapse_run
			log = uda.get_log()

	elapse = time.time() - start_time
	
	
	print("Problem : {} \n{}".format(prob.get_name(), prob.get_extra_info()))
	print("Best solution vector :\n {} \nBest fitness : {}".format(best_solution[1], best_solution[0]))
	print("Time of calculation of the best run : {}".format(str(timedelta(seconds=elapse_run))))
	print("Total time of calculation (over {} runs) : {}".format(epoch_runs, str(timedelta(seconds=elapse))))

	# Plot the convergence : Best fitness vs time and best fitness vs function evaluations
	x_time = np.arange(0, best_elapse_runs, best_elapse_runs/len(log))
	x_num = [row[1] for row in log]
	y = [row[2]  for row in log]

	if len(x_time) > len(y):
		x_time = x_time[:-1]
	elif len(x_time) < len(y):
		x_time.append(x_time[-1] + best_elapse_runs)

	assert(len(x_time)==len(y)), "Timing error !!! \n No worry, run again !"
	
	fig = plt.figure(figsize = (14,4))
	ax1 = fig.add_subplot(1,2,1)
	ax2 = fig.add_subplot(1,2,2)
	
	ax1.plot(x_time,y, color = "blue")
	ax1.set_title("Fitness vs time (best run)", fontsize=15)
	ax1.set_xlabel("Time (s)", fontsize = 14)
	ax1.set_ylabel("Best fitness", fontsize = 14)
	
	ax2.plot(x_num,y, color = "orange")
	ax2.set_title("Fitness vs Fevals (best run)",  fontsize=15)
	ax2.set_xlabel("Number of function evaluations", fontsize = 14)
	ax2.set_ylabel("Best fitness", fontsize = 14)
	plt.show()
	





