from Population import Population
from Family import two_point_crossover


if __name__ == "__main__":
    popu = Population()
    popu.create_families(two_point_crossover)
    
