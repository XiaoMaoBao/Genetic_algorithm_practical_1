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


#def experiment(crossover, eval):
#high, low
#n' = 0 
#n = 0
#runs = []
#success' = False
#while(n <= 1280 && !success')
#    (success, run') =  GA(n, crossover, eval)
#   if success == true
#       success' = success
#       n' = n
#       runs.append(run')
#   n = n*2
#       
#
#if n' != 0:
#   extra check if n' == 10,20 then return (n', run')
#
#   high = n'
#   low = n'/2
#   bi_number = bisection(low, high)
#   
#   tempRun = []
#   While(bi_number % 10 == 0):
#       bi_number = bisection(low,high)
#       fail_count = 0
#       for _ range(20):
#               (success,run') = GA (bi_number)
#               tempRun.append(run')
#
#               if(!success):
#                  fail_count +=1
#               if(fail_count >1):
#                   low = bi_number
#                   tempRun = []
#                   break
#               
#       if(failcount<2):     
#           n', high = bi_number
#           runs = tempRun 
#           
#    
#else: 
#   return (n', None)
#   
#return (n', runs)
#
#

#def GA(n, crossover, eval)
#run = Run()
#previous_fitness = 0 
#no_improvement = 0
#popu = GA(n, crossover, eval)
#
#while(no_improvement < 5)
#   run.starttimer
#   popu.new generation
#   run.endtimer
#   (currentfitness, optimum)= popu.optimum 
#
#   run.totalEval = popu.eval_calls
#   run.cpu = popu.gen_time
#
#   if(optimum):
#       return (true, run)  
#  
#   if(previous_fitness => currentfitness):
#       no_improvement+=1
#    else: 
#       previous_fitness = currentfitness  
#
#   
#return (False, None)

#def bisection(lb, ub):
#return int((lb+ub)/2)
#




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