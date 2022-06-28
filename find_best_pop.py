# function to find currently best population and respective returns

# trade() contains actual trading signals based on peaks 

def find_max_return_pop(data, length, pop):
    
    return_set = []
    
    print('initial pop:', pop)
    
    # goes over all populations and finds population with largest delta 
    for i in range(len(pop)):
        return_l = trade(data,length,pop[i][0],pop[i][1],pop[i][2],pop[i][3])
        sum_return = sum(np.array(return_l))
        return_set.append(sum_return)
    
    index_return_max = np.argmax(return_set)
    max_return = max(np.array(return_set))
    
    return pop[index_return_max], max_return
