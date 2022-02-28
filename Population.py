from audioop import cross
from Representation import String
from Family import Family, uniform_crossover, two_point_crossover
import random

STRING_LENGTH = 40
POPULATION_SIZE = 20

class Population:
    def __init__(self) -> None:
        self.strings = self.generate_pop()

    def generate_string(self):
        return String(''.join([random.choice(['0', '1']) for _ in range(STRING_LENGTH)]))
    
    def generate_pop(self):
        poplist = []
        for _ in range(POPULATION_SIZE):
            str = self.generate_string()
            print(str)
            poplist.append(str)
        return(poplist)
    
    def createGen(self, eval, crossover):
        newGen =[]
        #code breaks when shuffle is called
        #bug?
        # self.shuffle()
        families = self.create_families(crossover)

        for family in families:
            newGen.extend(family.tournament(eval))
        
        # print("new gen")
        # for string in newGen:
        #     print(string)
        
        self.strings  = newGen


    def shuffle(self) -> str:
        self.strings = random.shuffle(self.strings)

    def fitness_score(self, eval):
        return sum(map(lambda x: eval(x), self.strings))

    
    def create_families(self, crossover):
        families = []
        for i in range(int(POPULATION_SIZE/2)):
            family = Family(self.strings[i], self.strings[i+1])
            family.child1, family.child2 = crossover(family.parent1, family.parent2)
            families.append(family)
            i = i+1
        return families
