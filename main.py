from cProfile import run
from Population import Population
from Representation import count_ones, NonDeceptiveTight, DeceptiveTight, DeceptiveLoose, NonDeceptiveLoose
from Family import two_point_crossover
from Data import DataContainer, Run
import pandas as pd  
from time import process_time


if __name__ == "__main__":
    #TODO implement stopwatch
        #t1_start = process_time() 
        #t1_stop = process_time()
    #TODO implement list to csv
    #TODO create bisection function



    popu = Population(NonDeceptiveLoose, two_point_crossover)
    popu.iterate(iterations=5)
    # popu.createGen(DeceptiveTight,two_point_crossover)
    # print(popu.fitness_score(DeceptiveTight))


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


# 

middlebound
#   if x == 5:
#       Break: #Fail
#   if N > 10:
#       Succesfull then Bisection Search(N)
#       Return minimal population sizeB
isection Search N,lowhighN/2, NlowNhighNmidNmid()Nmid, Nhighe
lselow, Nmid
#    for z in 20 range()20_)                                            
    #       FAILCOUNTER++
#   FailAILCOUNTER = 0
#       If FAILCOUNTER == 2
#           Break:FAILCOUNTER == 2
if x == 5#           