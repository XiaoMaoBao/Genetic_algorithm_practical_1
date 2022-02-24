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
    
    def get_fittest(self):
        fittest  = []
        childs = [self.child1.count_ones(), self.child2.count_ones()].sort()
        parents = [self.parent1.count_ones(), self.parent1.count_ones()].sort()
        pass

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