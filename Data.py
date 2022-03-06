
import csv
class DataContainer:
    def __init__(self, _experiment_name) -> None:
        self.population_size=0 #found by bisection
        self.runs = []  
        self.experiment_name = _experiment_name  

    def export_to_csv():
        pass


   # filename = 'items.csv'
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


class Run:
    def __init__(self) -> None:
        self.fitness_eval_calls = 0
        self.generations = 0
        self.success = False
        
    
    def increment_fitness_calls(self, population_size ):
        # in one generation two fitness call for the parents 
        # two fitness call for the children 
        # one fitness call after the tournament
        # and one fitness call for optimum check
        self.fitness_eval_calls += (population_size * 4) + 2

    def increment_generations(self):
        self.generations += 1 
    
    def run_successful(self, _success):
        self.success = _success












#if a number N is successful start bisection
#for a value of a bisection we create a datacontainer 
#start 20 runs




