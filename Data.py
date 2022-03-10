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
            writer.writerow(["generation_number", "fitness_call", "cpu_time"])

            for run in data:
                if run is not None:
                    writer.writerow([run.generations, run.fitness_eval_calls, run.cpu_time])
    except BaseException as e:
        print('BaseException:', name)
    else:
        print('Data has been successfully saved!')



def export_optimizer_to_csv(name, data, optimizer):
    filename = name + "_" + str(data.cpu_time) + "_" + str(data.fitness_eval_calls)
    index = 0
    try:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["generation", "prop", "correct_selection", "error_selection", "schemata_1_count", "schemata_1_avg_fitness", "schemata_1_std", "schemata_0_count", "schemata_0_avg_fitness", "schemata_0_std" ])
            for opt in optimizer.gens:
                writer.writerow([index, opt.prop , opt.correct_selection, opt.error_selection, opt.schemata_1_count, opt.schemata_1_avg, opt.schemata_1_std, opt.schemata_2_count, opt.schemata_2_avg, opt.schemata_2_std])
                index+=1
    except BaseException as e:
        print('BaseException:', filename)
    else:
        print('Data has been successfully saved!')

       


class Generation:
    def __init__(self) -> None:
        self.prop = 0
        self.error_selection = 0
        self.correct_selection = 0


        self.schemata_1_strings = []
        self.schemata_2_strings = []


        self.schemata_1_count = 0
        self.schemata_2_count = 0

        self.schemata_1_std = 0
        self.schemata_2_std = 0

        self.schemata_1_avg = 0
        self.schemata_2_avg = 0
        

class GenerationContainer:
        def __init__(self) -> None:
            self.gens = [Generation()]
            self.current_gen = 0
        
        def increment_generation(self):
            self.gens.append(Generation())
            self.current_gen +=1




class Run:
    def __init__(self) -> None:
        self.fitness_eval_calls = 0
        self.generations = 0
        self.success = False
        self.timer_start = 0
        self.timer_stop = 0
        self.cpu_time =0
        self.popu_size = 0
        self.gens = []
        
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
    
