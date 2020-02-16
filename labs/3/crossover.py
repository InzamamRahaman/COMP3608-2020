import numpy as np 


def single_point(parent1, parent2):
    point = np.random.randint(1, len(parent1))
    child = np.zeros_like(parent1)
    child[:point] = parent1[:point]
    child[point:] = parent2[point:]
    return child


def interpolation(parent1, parent2):
    lambda_point = np.random.uniform()
    return lambda_point * parent1 +  (1 - lambda_point) * parent2

def uniform(parent1, parent2):
    selection = np.random.randint(0, 2, size=len(parent1))
    neg_selection = 1 - selection
    child = parent1 * selection + parent2 * neg_selection
    return child 