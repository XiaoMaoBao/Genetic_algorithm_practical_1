from Population import Population
from Representation import count_ones
from Family import two_point_crossover


if __name__ == "__main__":
    popu = Population()
    # families = popu.create_families(two_point_crossover)
    popu.createGen(count_ones,two_point_crossover)
    print(popu.fitness_score(count_ones))
