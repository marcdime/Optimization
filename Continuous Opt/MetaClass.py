import pygmo as pg
import numpy as np
import time
import matplotlib.pyplot as plt
import shift as sf
from math import pi
from matplotlib import cm
from datetime import timedelta

'''
shifted shere class
'''
class shifted_sphere(object):
	
	def __init__(self, dim, value_shift, biais):
		self.value_shift = value_shift
		self.biais = biais
		self.dim = dim

	
	def fitness(self, x):
		global value_shift
		global biais
		sphere = np.sum((x-self.value_shift[:len(x)])**2) + self.biais
		return [sphere]
	
	def get_bounds(self):
		return (np.array([-100] * self.dim), np.array([100] * self.dim))

	@property
	def dim(self):
		return self._dim
	@dim.setter	
	def dim(self, new_dim):
		self._dim = new_dim

	def get_offset(self):
		return 0
		
	
	def get_name(self):
		return "Shifted Sphere Function"

	def get_extra_info(self):
		return "Dimension : " + str(self.dim)
	
	
'''
shifted Schwefel class
'''
class shifted_Schwefel(object):
	
	def __init__(self, dim, value_shift, biais):
		self.value_shift = value_shift
		self.biais = biais
		self.dim = dim        
	
	def fitness(self, x):
		global value_shift
		global biais        
		schwefel = np.max(abs(x-self.value_shift[:len(x)])) + self.biais
		return [schwefel]
	
	def get_bounds(self):
		return (np.array([-100] * self.dim), np.array([100] * self.dim))

	@property
	def dim(self):
		return self._dim
	@dim.setter	
	def dim(self, new_dim):
		self._dim = new_dim

	def get_offset(self):
		return -440
	
	def get_name(self):
		return "Shifted Schwebel Function"

	def get_extra_info(self):
		return "Dimension : " + str(self.dim)

'''
shifted Rosenbrock class
'''
class shifted_Rosenbrock(object):
	
	def __init__(self, dim, value_shift, biais):
		self.value_shift = value_shift
		self.biais = biais
		self.dim = dim        
	
	def fitness(self, x):
		global value_shift
		global biais
		
		identity = np.ones(len(x))        
		z = x - self.value_shift[:len(x)] + identity
		rosen = [100*(z[i]**2 - z[i+1])**2 + (z[i+1]-1)**2 for i in range(len(x) - 1)] 
		return [np.sum(rosen) + self.biais]
				
	def get_bounds(self):
		return (np.array([-100] * self.dim), np.array([100] * self.dim))

	@property
	def dim(self):
		return self._dim
	@dim.setter	
	def dim(self, new_dim):
		self._dim = new_dim  

	def get_offset(self):
		return 0  	     
			
	def get_name(self):
		return "Shifted Rosenbrock Function"

	def get_extra_info(self):
		return "Dimension : " + str(self.dim)


'''
shifted Rastrigin class
'''
class shifted_Rastrigin(object):
	
	def __init__(self, dim, value_shift, biais):
		self.value_shift = value_shift
		self.biais = biais
		self.dim = dim        
	
	def fitness(self, x):
		global value_shift
		global biais
		
		identity_10 = np.full((len(x),),10)        
		z = x - self.value_shift[:len(x)]
		rastrigin = np.sum(z**2 - 10*np.cos(2*pi*z) + identity_10) + self.biais  
		return [rastrigin]
				
	def get_bounds(self):
		return (np.array([-5] * self.dim), np.array([5] * self.dim))


	@property
	def dim(self):
		return self._dim
	@dim.setter	
	def dim(self, new_dim):
		self._dim = new_dim

	def get_offset(self):
		return -330
				
	def get_name(self):
		return "Shifted Rastrigin Function"

	def get_extra_info(self):
		return "Dimension : " + str(self.dim)


'''
shifted Griewank class
'''
class shifted_Griewank(object):
	
	def __init__(self, dim, value_shift, biais):
		self.value_shift = value_shift
		self.biais = biais
		self.dim = dim        
	
	def fitness(self, x):
		global value_shift
		global biais
		z = x - self.value_shift[:len(x)]
		f1 = 1
		griewank = 0
		for i in range(len(x)-1):
			f1 = f1*np.cos(z[i]/np.sqrt(i+1))
			griewank += z[i]**2/4000 + f1 + 1 + self.biais  
		return [griewank]
				
	def get_bounds(self):
		return (np.array([-600] * self.dim), np.array([600] * self.dim))

	@property
	def dim(self):
		return self._dim
	@dim.setter	
	def dim(self, new_dim):
		self._dim = new_dim

	def get_offset(self):
		return -190

				
	def get_name(self):
		return "Shifted Griewank Function"

	def get_extra_info(self):
		return "Dimension : " + str(self.dim)

'''
shifted Ackley class
'''
class shifted_Ackley(object):
	
	def __init__(self, dim, value_shift, biais):
		self.value_shift = value_shift
		self.biais = biais
		self.dim = dim        
	
	def fitness(self, x):
		global value_shift
		global biais
		z = x - self.value_shift[:len(x)]
		f1 = np.sum(z**2)
		f2 = np.sum(np.cos(2*pi*z))
		ackley = -20*np.exp(-0.2*np.sqrt(f1/len(x))) - np.exp(f2/len(x)) + 20 + np.exp(1) + self.biais  
		return [ackley]
				
	def get_bounds(self):
		return (np.array([-32] * self.dim), np.array([32] * self.dim))

	@property
	def dim(self):
		return self._dim
	@dim.setter	
	def dim(self, new_dim):
		self._dim = new_dim

	def get_offset(self):
		return -138.5
				
	def get_name(self):
		return "Shifted Ackley Function"

	def get_extra_info(self):
		return "Dimension : " + str(self.dim)







