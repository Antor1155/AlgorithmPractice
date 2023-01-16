L = 100
sizes =  [ 1, 3, 5, 10, 30, 50, 75]
prices = [ 0.1, 0.2, 0.4, 0.9, 3.1, 5.1, 8.2]


def maxRevenue_Memoize_With_Solution_Recovery(L, sizes, prices): 
    T = [0]*(L+1)    # create an array of size L+1 and fill it with all 0s 
    S = [-1] * (L+1) # create an array to also record the best option for each l
                     # let us use -1 for the "waste" option
    k = len(sizes)
    assert len(prices) == k
    
    for l in range(1, L+1):
        T[l] = 0
        # compute the value for each cut with the corresponding cut 
        optionsWithSolutions = [(prices[i] + T[l-sizes[i]], i) for i in range(k) if l - sizes[i] >= 0]
        optionsWithSolutions.append ((0, -1)) # also keep the option of wasting
        # The above code is in python using comprehensions.
        # if you are a python newbie still, this is equivalent code below
        ## BEGIN ALTERNATIVE CODE
        # bestOptionSoFar = -1 # Let us us -1 for the waste option
        # for i in range(k): ## Iterate through all options
            # li = sizes[i]
            # if l - li >= 0:
                # option_value = prices[i] + T[l - li]
                # if option_value > T[l]:
                    # T[l] = option_value
                    # bestOptionSoFar = i
        #S[l] = bestOptionSoFar
        (T[l], S[l]) = max(optionsWithSolutions) # max of a tuple compares lexicographically 
    # Now for solution recovery
    cuts = []
    l = L
    while l > 0:
        option_id = S[l] # Which option gave the best result for l?
        if option_id >= 0:  # If it is an option that involves a cut
            cuts.append(sizes[option_id]) # Add the cut to the list
            l = l - sizes[option_id] # Reduce the remaining size
        else:  
            break  # If best option is to waste, then we are done
    return T[L], (cuts) # Returen max revenue and list of cuts




print(maxRevenue_Memoize_With_Solution_Recovery(50, sizes, prices))

print(maxRevenue_Memoize_With_Solution_Recovery(130, sizes, prices))