from audioop import cross
from tokenize import Double
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

        #TODO create generationcontainer

        self.strings = self.generate_pop()
        self.fitness = self.fitness_score()

        #TODO call for generation t = 0
        print(f"Initial population has fitness: {self.fitness}")

    def generate_string(self):
        return String(''.join([random.choice(['0', '1']) for _ in range(STRING_LENGTH)]))
    
    def generate_pop(self):
        poplist = []
        for _ in range(self.size):
            str = self.generate_string()
            str.fitness_score = self.eval(str)
            print(str)
            poplist.append(str)
        return(poplist)
    

    def create_gen(self, optimize = False):
        newGen =[]
        self.shuffle()
        families = self.create_families()

        for family in families:
            winners = family.tournament(self.eval)
            #TODO call selection check for gen t
            newGen.extend(winners)
        
        # print("new gen")
        # for string in newGen:
        #     print(string)
        
        self.strings = newGen
        self.fitness = self.fitness_score()        
        #TODO call schemata for gen t
        #TODO call prop for gen t

    def check_optimum(self):
        opt = False
        for x in self.strings:
            if x.fitness_score == STRING_LENGTH:
                opt = True

        return (self.fitness, opt)

    def selection_check(parents, winners):
        parent_1 = parents[0]
        parent_2 = parents[1]
        winner_1 = winners[0]
        winner_2 = winners[1]
        corr = 0
        err = 0 
        for i in range(0, STRING_LENGTH):
            if parent_1[i:i+1].count('1') is not parent_2[i:i+1].count('1'):
                if winner_1[i:i+1].count('1') == 1 and winner_2[i:i+1].count('1') == 1:
                    corr +=1

                elif (winner_1[i:i+1].count('1') == 0 and winner_2[i:i+1].count('1') == 0):
                    err+=1

        return (corr, err)   

    def prop(self, t):
        (_, opt) = self.check_optimum()
        if (opt):
            return 1
        count_ones = 0
        for x in self.strings:
            count_ones += x.count('1')

        return Double((self.size*STRING_LENGTH) / count_ones)
        

    def shuffle(self) -> str:
        self.strings = random.sample(self.strings, len(self.strings))

    def fitness_score(self):
        return sum(map(lambda x: x.fitness_score, self.strings))

    def create_families(self, optimize = False):
        families = []
        for i in range(int(self.size/2)):
            family = Family(self.strings[i], self.strings[i+1])
            family.child1, family.child2 = self.crossover(family.parent1, family.parent2)

            family.child1.fitness_score = self.eval(family.child1)
            family.child2.fitness_score = self.eval(family.child2)

            families.append(family)
            i = i+1
        return families



    def iterate(self, iterations: int):
        for i in range(iterations):
            self.create_gen()
            print(f"Generation {i+1} has fitness {self.fitness}")