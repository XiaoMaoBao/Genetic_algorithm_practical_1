from audioop import cross
from cProfile import run
from pickle import TRUE
from Population import Population
from Representation import count_ones, NonDeceptiveTight, DeceptiveTight, DeceptiveLoose, NonDeceptiveLoose
from Family import two_point_crossover, uniform_crossover
from Data import Run, export_to_csv,export_optimizer_to_csv



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
        fails = 0
        for _ in range(20):
            
            (success, run) = GA(n, crossover, eval, trap)
            if (success):
                runs.append(run)
            else: 
                fails +=1

            if fails > 1:
                break
        
        if fails <= 1:
            success_prime = success
            n_prime = n
        else:
            n = n*2
            runs = []


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
            for _ in range(20):
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
        return (n_prime, [])

    return (n_prime, runs)


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
        #string heeft 40 
        (current_fitness, opt) = popu.check_optimum()
        if trap:
            #each new generation n parent eval calls and n children eval calls times 10 since we have 10 subfunctions
            run.fitness_eval_calls += n*2*10
        else:
            #each new generation n parent eval calls and n children eval calls 
            run.fitness_eval_calls += n*2

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

def optimize_experiment(crossover, trap = False):
    n = 200

    run = Run()
    previous_fitness = 0
    no_improvement = 0
    popu = Population(count_ones, crossover, n)
    run.popu_size = n
    while(no_improvement < 5):
        run.startTimer()
        popu.create_gen(TRUE)
        run.stopTimer()

        (current_fitness, opt) = popu.check_optimum()
        if trap:
            run.fitness_eval_calls +=800
        else:
            run.fitness_eval_calls += 80

        run.increment_generations()

        if(opt):
            return (run, popu.optimize_container, opt)

        
        if previous_fitness >= current_fitness:
            no_improvement +=1
        else:
            previous_fitness = current_fitness

    return (run, popu.optimize_container, False)


if __name__ == "__main__":
    # (data_run, optimizer, flag) = optimize_experiment(uniform_crossover)
    # export_optimizer_to_csv("Optimizer_U_counting_ones", data_run, optimizer)

    # (data_run, optimizer, flag) = optimize_experiment(two_point_crossover)
    # export_optimizer_to_csv("Optimizer_T_counting_ones", data_run, optimizer)

    # (n, data) = experiment(uniform_crossover,count_ones, False)
    # filename= "exp_1_U" + str(n)
    # export_to_csv(filename, data)
    # (n, data) = experiment(two_point_crossover,count_ones, False)
    # filename= "exp_1_T" + str(n)
    # export_to_csv(filename, data)

    # (n, data) = experiment(uniform_crossover, DeceptiveTight, False)
    # filename= "exp_2_U" + str(n)
    # export_to_csv(filename, data)
    # (n, data) = experiment(two_point_crossover,DeceptiveTight, False)
    # filename= "exp_2_T" + str(n)
    # export_to_csv(filename, data)

    # (n, data) = experiment(uniform_crossover,NonDeceptiveTight, False)
    # filename= "exp_3_U" + str(n)
    # export_to_csv(filename, data)
    # (n, data) = experiment(two_point_crossover,NonDeceptiveTight, False)
    # filename= "exp_3_T" + str(n)
    # export_to_csv(filename, data)

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

    


