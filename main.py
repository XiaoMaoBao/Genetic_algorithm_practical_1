from audioop import cross
from cProfile import run
from Population import Population
from Representation import count_ones, NonDeceptiveTight, DeceptiveTight, DeceptiveLoose, NonDeceptiveLoose
from Family import two_point_crossover, uniform_crossover
from Data import Run, export_to_csv



    # popu = Population(NonDeceptiveLoose, two_point_crossover)
    # popu.iterate(iterations=5)
    # popu.createGen(DeceptiveTight,two_point_crossover)
    # print(popu.fitness_score(DeceptiveTight))

def experiment(crossover, eval, trap):
    n_prime = 0
    n = 10
    runs = []
    success_prime = False

    while((n <= 1280) and (not success_prime)):
        (success, run) = GA(n, crossover, eval, trap)
        if (success):
            success_prime = success
            n_prime = n
            runs.append(run)
        
        n = n*2


    if n_prime != 0:
        if n_prime == 10 or n_prime == 20:
            return (n_prime, runs)
        
        high = n_prime
        low = int(n_prime/2)
        mid = bisection(low,high)

        temp_runs = []
        while(mid % 10 == 0):
            temp_runs = []
            mid = bisection(low,high)
            fail_count = 0
            for index in range(20):
                (_success, _run) = GA(mid, crossover, eval,trap)
                temp_runs.append(_run)

                if not _success:
                    fail_count +=1
                if fail_count > 1:
                    low = mid
                    temp_runs = []
                    break                    

            if fail_count < 2 and mid % 10 == 0:
                n_prime = mid
                high = mid
                runs = temp_runs
                temp_runs = []
    else:
        return (n_prime, None)

    return (n_prime, runs)



#counting ones
#1 gen: 
#40 parents
#40 children
#------tournament------
# van de 80 haal je 40 
#
# 40 check voor een opt + fitness score
# 


def GA(n, crossover, eval, trap):
    run = Run()
    previous_fitness = 0
    no_improvement = 0
    popu = Population(eval, crossover, n)
    run.popu_size = n
    while(no_improvement < 5):
        run.startTimer()
        popu.create_gen()
        run.stopTimer()

        (current_fitness, opt) = popu.check_optimum()
        if trap:
            run.fitness_eval_calls +=800
        else:
            run.fitness_eval_calls += 80

        run.increment_generations()

        if(opt):
            return (True, run)
        
        if previous_fitness >= current_fitness:
            no_improvement +=1
        else:
            previous_fitness = current_fitness

    return (False, None)
        

def bisection(lb,ub):
    return int((lb+ub)/2)



if __name__ == "__main__":
    (n, data) = experiment(uniform_crossover,count_ones, False)
    filename= "exp_1_U" + str(n)
    export_to_csv(filename, data)
    (n, data) = experiment(two_point_crossover,count_ones, False)
    filename= "exp_1_T" + str(n)
    export_to_csv(filename, data)

    (n, data) = experiment(uniform_crossover, DeceptiveTight, False)
    filename= "exp_2_U" + str(n)
    export_to_csv(filename, data)
    (n, data) = experiment(two_point_crossover,DeceptiveTight, False)
    filename= "exp_2_T" + str(n)
    export_to_csv(filename, data)

    (n, data) = experiment(uniform_crossover,NonDeceptiveTight, False)
    filename= "exp_3_U" + str(n)
    export_to_csv(filename, data)
    (n, data) = experiment(two_point_crossover,NonDeceptiveTight, False)
    filename= "exp_3_T" + str(n)
    export_to_csv(filename, data)

    (n, data) = experiment(uniform_crossover,DeceptiveLoose, False)
    filename= "exp_4_U" + str(n)
    export_to_csv(filename, data)
    (n, data) = experiment(two_point_crossover,DeceptiveLoose, False)
    filename= "exp_4_T" + str(n)
    export_to_csv(filename, data)

    (n, data) = experiment(uniform_crossover,NonDeceptiveLoose, False)
    filename= "exp_5_U" + str(n)
    export_to_csv(filename, data)
    (n, data) = experiment(two_point_crossover,NonDeceptiveLoose, False)
    filename= "exp_5_T" + str(n)
    export_to_csv(filename, data)

    




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
#   x = 0
    #   previous ttotalfitness = 0
    #       previous totalprevious totalfitness = totalfitnessCalc Fitness of Poppuu, and PIndiviualpppppppppp


# 

# middlebound
# #   if x == 5:
# #       Break: #Fail
# #   if N > 10:
# #       Succesfull then Bisection Search(N)
# #       Return minimal population sizeB
# isection Search N,lowhighN/2, NlowNhighNmidNmid()Nmid, Nhighe
# lselow, Nmid
# #    for z in 20 range()20_)                                            
#     #       FAILCOUNTER++
# #   FailAILCOUNTER = 0
# #       If FAILCOUNTER == 2
# #           Break:FAILCOUNTER == 2
# if x == 5#           