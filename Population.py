from audioop import cross
from Representation import String
from Family import Family, uniform_crossover, two_point_crossover
from Data import  Run
import random

STRING_LENGTH = 40


class Population:
    def __init__(self, eval, crossover, population_size) -> None:
        self.crossover = crossover
        self.eval = eval
        self.size = population_size
        self.eval_calls = 0

        self.strings = self.generate_pop()
        self.fitness = self.fitness_score()
        print(f"Initial population has fitness: {self.fitness}")

    def generate_string(self):
        return String(''.join([random.choice(['0', '1']) for _ in range(STRING_LENGTH)]))
    
    def generate_pop(self):
        poplist = []
        for _ in range(self.size):
            str = self.generate_string()
            print(str)
            poplist.append(str)
        return(poplist)
    

    def create_gen(self):
        newGen =[]
        self.shuffle()
        families = self.create_families()

        for family in families:
            newGen.extend(family.tournament(self.eval))
        
        # print("new gen")
        # for string in newGen:
        #     print(string)
        
        self.strings = newGen
        self.fitness = self.fitness_score()        

    def reset_fitness_calls(self):
        self.eval_calls= 0


    def check_optimum(self):
        score_sum = 0
        opt = False
        for x in self.strings:
            fitness = self.eval(x)
            score_sum += fitness
            if (self.eval(x) == STRING_LENGTH):
                opt = True

        return (score_sum, opt)

    def shuffle(self) -> str:
        self.strings = random.sample(self.strings, len(self.strings))

    def fitness_score(self):
        self.eval_calls +=1
        return sum(map(lambda x: self.eval(x), self.strings))

    def create_families(self):
        families = []
        for i in range(int(self.size/2)):
            family = Family(self.strings[i], self.strings[i+1])
            family.child1, family.child2 = self.crossover(family.parent1, family.parent2)
            families.append(family)
            i = i+1
        return families

    def iterate(self, iterations: int):
        for i in range(iterations):
            self.create_gen()
            print(f"Generation {i+1} has fitness {self.fitness}")