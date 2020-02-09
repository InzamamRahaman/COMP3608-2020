import numpy as np 

def single_point_crossover(parent1, parent2):
    crossover_point = np.random.uniform(1, len(parent1))
    child = np.zeros_like(parent1)
    child[:crossover_point] = parent1[:crossover_point]
    child[crossover_point:] = parent2[crossover_point:]
    return child 

def uniform_crossover(parent1, parent2):
    child = np.zeros_like(parent1)
    selector = np.random.random(size=len(parent2)) >= 0.5 
    child = selector * parent1 + (~selector) * parent2
    return child 

def interpolation_crossover(parent1, parent2, lam=None):
    if lam is None:
        lam = np.random.uniform(0.1, 1.0)
    return (1 - lam) * parent2 + lam * parent1

