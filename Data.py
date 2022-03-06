
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






