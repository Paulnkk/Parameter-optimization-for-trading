# function generates best population and return for best population (max return) over whole dataset

# data...is time series where optimization is exectued
# all parameters...are similar to init_params.py

def genetic_opt(data, length, height_up_range_upper,height_up_range_lower, r1_range_upper, r1_range_lower, r2_range_upper, r2_range_lower, dist_max_range_upper, dist_max_range_lower, n):
    
    # generate initial population -> initial sets of different parameters 
    pop_init = init_genetic_peaks_trade(height_up_range_upper,height_up_range_lower, r1_range_upper, r1_range_lower, r2_range_upper, r2_range_lower, dist_max_range_upper, dist_max_range_lower, n)
    
    # select set of parameters with max return
    best_pop, max_ret = find_max_return_pop(data, length, pop_init)
    
    # init parameters for genetic optimization 
    f_best = max_ret    
    exp_return = 0.1
    p_mut = []
    
    # mutation rate
    F = 0.8
    
    # we loop over populations until we find one that is higher than the return we apply
    while f_best < exp_return:
      
        # we calculate p_mut for the 'best' population -> highest return
        for i in range(len(best_pop)):
            
            # i is the parameter index 
            diff = find_2_random_p(pop_init, i)
            
            # operation for mutation
            p_mut_k = best_pop[i] + F * (diff)
            
            # p_mut vector for all parameters 
            p_mut.append(p_mut_k)
            
        best_pop_old = best_pop
        
        CR = 0.7
        
        # we generate potential new best population
        for i in range(len(best_pop)):
            R = random.uniform(0, 1)
            
            if R < CR:
                best_pop[i] = p_mut[i]
            else:
                best_pop[i] = best_pop_old[i]
        
        
        f_best_2_list = trade(data,length,best_pop[0],best_pop[1],best_pop[2],best_pop[3])
        f_best_1_list = trade(data,length,best_pop_old[0],best_pop_old[1],best_pop_old[2],best_pop_old[3])
        
        
        f_best_2 = sum(np.array(f_best_2_list))
        f_best_1 = sum(np.array(f_best_1_list))
        
        
        if f_best_2 > f_best_1:
            f_best = f_best_2
            best_pop = best_pop
        else:
            f_best = f_best_1
            best_pop = best_pop_old

    return f_best, best_pop
