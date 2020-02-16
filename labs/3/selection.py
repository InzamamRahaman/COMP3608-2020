import numpy as np 


def top_k(arr, k):
    return np.argpartition(arr, -k)[:k]

def elitism(e, population, fitnesses):
    top = top_k(fitnesses, e)
    return population[top]

class Selector(object):
    def __init__(self):
        super().__init__()

    def prep_selector(self, fitnesses):
        pass 

    def select(self, population):
        pass 


class RouletteWheelSelector(Selector):
    def __init__(self):
        super().__init__()
        self.table = []
    
    def prep_selector(self, fitnesses):
        transformed = np.exp(fitnesses)
        total = np.sum(transformed)
        self.table = transformed / total 
        self.indicies = np.arange(0, len(fitnesses), 1, dtype=np.int)

    def select(self, population):
        parent1_idx, parent2_idx = np.random.choice(self.indicies, size=2, replace=False, p=self.table)
        parent1 = population[parent1_idx, :]
        parent2 = population[parent2_idx, :]
        return parent1, parent2

class TournamentSelection(Selector):
    def __init__(self):
        super().__init__()
        self.table = []
    
    def prep_selector(self, fitnesses):
        self.table = fitnesses

    def select(self,population):
        indicies = np.arange(0, len(population) + 1, 1, dtype=np.int)
        sub_population = population[indicies]
        sub_pop_fitnesses = self.table[indicies]
        parent1_idx, parent2_idx = top_k(sub_pop_fitnesses, 2)
        return sub_population[parent1_idx], sub_pop_fitnesses[parent2_idx]