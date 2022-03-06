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





#while i <= 20
# n =10 
# do GA(n)
#   in GA(n) if the generatio
# check opt: yes = stop, increase i and do GA (n) again, no = increase n'= n*2, i = 1, do GA(n')
# if i == 19: GA with popu N is success 
# 
#


# iterations = 20
# for every iteration:
#   create population with size 10
#   Search for global optimum:
#       If found: return
#       If not found: double population size and search again
#   
# 

#28
#ing0 stop Fa toil 
#sed rn keeei  iepf succesful if N>= 1 go
#u#  do run see if ccesfull, if not dubble sizeicfGenerate population with size 10or i in range(20):
#  
# 
# 
# 
# 
#160+320 = 480/2
#midpoint = 240
#320 + 240 = 560/2
#midpoint 280
#240 + 280 = 520/2
#midpoint 260
#280 + 260 = 540/2
#midpoint = 270
#260 + 270 = 530/2
#midpoint 265
#270  +265 = 535/2
#a  b
#160    320
#240    320
#240    280
#260    280
#260    270
#270    275




#10,20,40,80,160,320,640,1280
#320 found
#diff(160,320) =160/2 = 80
#new 320-80 = 240
#diff(320,240) = 80/2 = 40
#new 320 - 40 = 280
#diff(240,280) =40/2 20
#new 280 -20 = 260
#diff(280,260) = 20/2
#new 280-10  =270
#160 - 320= 240
#240 - 320 = 280
#280 - 320 = 

#dataclass 
#String experiment
#The population size N
#for each run of N
#the run number
#The number of fitness evaluation cals
#The number of new generations
#The running time


#dataclass object
#string experiment name
#Fixed var N = 320
#array of a run
#a run tracks
#   -The number of fitness evaluation calls
#   -The number of new generations
#   -The running time


