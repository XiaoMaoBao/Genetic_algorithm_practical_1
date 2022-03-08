from ast import Not
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


def export_to_csv(name,data):
    try:
        with open(name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["generatio_number", "fitness_call", "cpu_time"])
            for run in data:
                if run is not None:
                    writer.writerow([run.generations, run.fitness_eval_calls, run.cpu_time])
    except BaseException as e:
        print('BaseException:', name)
    else:
        print('Data has been successfully saved!')





    #filename = 'items.csv'
# items = [Run(), Run(), Run()]
# try:
#     with open(filename, 'w', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(["calls", "gen", "time"])

#         for item in items:
#             writer.writerow([item.fitness_eval_calls, item.generations, item.running_time])
# except BaseException as e:
#     print('BaseException:', filename)
# else:
#     print('Data has been loaded successfully !')

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
#   x = 0
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
        self.popu_size = 0
        
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
        self.cpu_time = abs(self.timer_start - self.timer_stop)
    
