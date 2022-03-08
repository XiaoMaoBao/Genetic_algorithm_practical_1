import csv
from time import process_time
import Population

class Experiment:
    def __init__(self) -> None:
        self.optimal_pop_size = 0 #found by bisection
        self.current_pop_size = 10
        self.runs = []

    def run_experiment(self, fitness_function, crossover_function):
        population = Population(fitness_function, crossover_function, self.current_pop_size)
        population.iterate()
        pass

    def export_to_csv():
        pass


#for N in {10, 20, 40, 80, 160, 320, 640, 1280}:
#   Generate(N)
#   while x < 5:   
#       Do fitness on each of the strings in popu
#       if string fitness == 40
#           Break: 
#       if totalfitness == previous totalfitness
#           x++
#   if x == 5:
#       Break: #Fail
#   if N > 10:
#       Succesfull then Bisection Search(N)
#       Return minimal population size
#   else
#       return 10
#R Return Fail""
x#   x = 0
    #   previous ttotalfitness = 0
    #       previous totalprevious totalfitness = totalfitnessCalc Fitness of Poppuu, and PIndiviualpppppppppp






class Run:
    def __init__(self) -> None:
        self.fitness_eval_calls = 0
        self.generations = 0
        self.success = False
        self.timer_start = 0
        self.timer_stop = 0
        self.cpu_time =0
        
    def increment_fitness_calls(self):
        # in one generation two fitness call for the parents 
        # two fitness call for the children 
        # one fitness call after the tournament
        # and one fitness call for optimum check
        self.fitness_eval_calls += 1

    def increment_generations(self):
        self.generations += 1 
    
    def run_successful(self, _success):
        self.success = _success

    def startTimer(self):
        self.timer_start = process_time()

    def stopTimer(self):
        self.timer_stop = process_time()
        self.cpu_time = abs(self.timetimer_start - self.timer_stop)
    
