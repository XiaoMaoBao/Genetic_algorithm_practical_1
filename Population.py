from audioop import cross
from tokenize import Double
from Representation import String
from Family import Family, uniform_crossover, two_point_crossover
from Data import  Run, GenerationContainer
from statistics import mean, stdev

import random

STRING_LENGTH = 40


class Population:
    def __init__(self, eval, crossover, population_size) -> None:
        self.crossover = crossover
        self.eval = eval
        self.size = population_size

        #TODO create generationcontainer
        self.optimize_container = GenerationContainer()

        self.strings = self.generate_pop()
        self.fitness = self.fitness_score()

        #TODO call for generation t = 0 1 and 3
        self.prop(self.optimize_container.current_gen)
        self.schemata(self.optimize_container.current_gen)

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
        if (optimize):
            self.optimize_container.increment_generation()

        self.shuffle()
        families = self.create_families()

        for family in families:
            winners = family.tournament(self.eval)

            #TODO call selection check for gen t
            if(optimize):
                self.selection_check( [family.parent1, family.parent2], winners, self.optimize_container.current_gen)
            newGen.extend(winners)
        

        self.strings = newGen
        self.fitness = self.fitness_score()        
        #TODO call schemata for gen t
        #TODO call prop for gen t
        if optimize:
            self.prop(self.optimize_container.current_gen)
            self.schemata(self.optimize_container.current_gen)

    def check_optimum(self):
        opt = False
        for x in self.strings:
            if x.fitness_score == STRING_LENGTH:
                opt = True

        return (self.fitness, opt)

    def selection_check(self, parents, winners, t):
        parent_1 = parents[0]
        parent_2 = parents[1]
        winner_1 = winners[0]
        winner_2 = winners[1]
        corr = 0
        err = 0 
        for i in range(0, STRING_LENGTH):
            if parent_1.slice(i,i+1).count('1') is not parent_2.slice(i,i+1).count('1'):
                if winner_1.slice(i,i+1).count('1') == 1 and winner_2.slice(i,i+1).count('1') == 1:
                    corr +=1

                elif (winner_1.slice(i,i+1).count('1') == 0 and winner_2.slice(i,i+1).count('1') == 0):
                    err+=1
        
        self.optimize_container.gens[t].error_selection += err
        self.optimize_container.gens[t].correct_selection += corr

    def prop(self, t):
        if t == 0:
            self.optimize_container.gens[t].prop= 0.5
            return
    
        (_, opt) = self.check_optimum()
        if (opt):
             self.optimize_container.gens[t].prop= 1
             return 
        
        count_ones = 0
        for x in self.strings:
            count_ones += x.count('1')
        _prop = (count_ones / (self.size*STRING_LENGTH))
        self.optimize_container.gens[t].prop =  _prop
        
    def schemata(self, t):
        for x in self.strings:
            xs = x.slice(0,1)
            if xs == '1':
                self.optimize_container.gens[t].schemata_1_strings.append(x)
            else:
                self.optimize_container.gens[t].schemata_2_strings.append(x)

        schemata_1_strings_score = [x.fitness_score for x in self.optimize_container.gens[t].schemata_1_strings ]
        schemata_2_strings_score = [x.fitness_score for x in self.optimize_container.gens[t].schemata_2_strings ]

        self.optimize_container.gens[t].schemata_1_count = len(self.optimize_container.gens[t].schemata_1_strings)
        self.optimize_container.gens[t].schemata_2_count = len(self.optimize_container.gens[t].schemata_2_strings)


        if len(schemata_1_strings_score) > 0:
            self.optimize_container.gens[t].schemata_1_avg = mean(schemata_1_strings_score)

        if len(schemata_2_strings_score) > 0:
            self.optimize_container.gens[t].schemata_2_avg = mean(schemata_2_strings_score)

        if len(schemata_1_strings_score) > 1:
            self.optimize_container.gens[t].schemata_1_std = stdev(schemata_1_strings_score)
        
        if len(schemata_2_strings_score) > 1:
            self.optimize_container.gens[t].schemata_2_std = stdev(schemata_2_strings_score)





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