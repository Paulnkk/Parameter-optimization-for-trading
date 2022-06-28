# function to initialize start parameters for optimization 
# height_up_range_lower, height_up_range_upper...lower and upper bound for parameter 1 (height_up)
# r1_range_lower, r1_range_upper...lower and upper bound for parameter 2 (r1)
# r2_range_lower, r2_range_upper...lower and upper bound for parameter 3 (r2)
# dist_max_range_lower, dist_max_range_upper...lower and upper bound for parameter 4 (dist_max)

def init_genetic_peaks_trade(height_up_range_upper,height_up_range_lower, r1_range_upper, r1_range_lower, r2_range_upper, r2_range_lower, dist_max_range_upper, dist_max_range_lower, n):
    
    pop_start = []
    
    for i in range(1, n+1):
        
        #height_up
        p0 = random.uniform(height_up_range_lower, height_up_range_upper)
        #dist_max
        p1 = random.randint(dist_max_range_lower, dist_max_range_upper) 
        #r1
        p2 = random.uniform(r1_range_lower, r1_range_upper)
        #r2
        p3 = random.uniform(r2_range_lower, r2_range_upper)
        
        x_i = [p0, p1, p2, p3]
        
        pop_start.append(x_i)
    
    return pop_start
