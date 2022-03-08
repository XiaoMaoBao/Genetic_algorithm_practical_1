from Representation import String
import random

STRING_LENGTH = 40

class Family:
    def __init__(self, parent1: String, parent2: String) -> None:
        self.parent1 = parent1
        self.parent2 = parent2
        self.child1, self.child2 = None, None
        
    def set_children(self, child1, child2):
        self.child1, self.child2 = child1, child2
    
    def tournament(self, eval):
        fittest = []

        childs = [self.child1, self.child2]
        parents = [self.parent1, self.parent2]

        childs.sort(key=lambda x:x.fitness_score)
        parents.sort(key=lambda x:x.fitness_score)

        index_p = 1
        index_c = 1
        if childs[0].fitness_score >= parents[1].fitness_score:
            return childs

        while(len(fittest) < 2):
            child_fit = childs[index_c]
            parent_fit = parents[index_p]

            if(child_fit.fitness_score >= parent_fit.fitness_score):
                fittest.append(child_fit)
                index_c -=1
            else:
                fittest.append(parent_fit)
                index_p -=1

        return fittest

def uniform_crossover(parent1: String, parent2: String):
    idx = random.choice(range(1, STRING_LENGTH))
    child1 = String(parent1.binary_str[:idx] + parent2.binary_str[idx:])
    child2 = String(parent2.binary_str[:idx] + parent1.binary_str[idx:])
    return child1, child2

def two_point_crossover(parent1: String, parent2: String):
    idx1, idx2 = sorted(random.sample(range(1, STRING_LENGTH), 2))
    child1 = String(parent1.binary_str[:idx1] + parent2.binary_str[idx1:idx2] + parent1.binary_str[idx2:])
    child2 = String(parent2.binary_str[:idx1] + parent1.binary_str[idx1:idx2] + parent2.binary_str[idx2:])
    return child1, child2