# Important, Run this cell below
W = 200 # weight limit is 200
weights = [1, 5, 20, 35, 90] # These are the weights of individual items
values = [15, 14.5, 19.2, 19.8, 195.2] # These are the values of individual items


def memoizedMaxStealZeroOne(W, weights, values): 
    n = len(weights)
    assert (len(values) == n), 'Weights and Values list must be of same size'
    assert (W >= 0)
    if W == 0: 
        return 0, []# nothing to steal and 0 value derived.
    
    # Initialize the memo table as a list of lists
    # fill in all entries with a zero
    T = [ [0 for j in range(n)] for w in range(W+1)]
    S = [ [0 for j in range(n)] for w in range(W+1)]

    # we will use this helper method to access our memo table.
    # it will save us a lot of code later.
    def getTblEntry(w, j): 
        if w == 0: 
            return 0
        if w < 0: 
            return -float('inf')
        if j >= n:
            return 0
        return T[w][j]

    for w in range(1, W+1): # w in ascending order from 1 to W.
        for j in range(n-1, -1, -1):  # this is a descending order loop from n-1 to 0.
            # this allows us to simultaneously fill T, S without using if-then-else loop
            (T[w][j], S[w][j]) = max(
                (values[j] + getTblEntry(w - weights[j], j+1), 1), 
                (getTblEntry(w, j+1), 0))
    itemsToSteal = [] 
    # recover solution
    weightOfKnapsack = W  
    for j in range(n): 
        if (S[weightOfKnapsack][j] == 1):
            itemsToSteal.append(j)
            weightOfKnapsack = weightOfKnapsack - weights[j]
            print(f'Steal Item {j}: Weight = {weights[j]}, Value = {values[j]}')
    print(f'Total weight stolen: {W - weightOfKnapsack}, value = {T[W][0]}')
    return (T[W][0], itemsToSteal)
            
    
memoizedMaxStealZeroOne(W, weights, values)



def maxSteal_memo(W, weights, values):
    # Initialize the tables
    T = [0]* (W+1)
    S = [-1]* (W+1)
    k = len(weights)
    assert len(values) == k
    for w in range(1, W+1):
        opts =  [  ( (values[i]+ T[ w - weights[i] ]), i )  for i in range(k) if w - weights[i] >= 0 ]
        opts.append( (-float('inf'), -1) ) # In case opts was empty from the previous step.
        T[w], S[w] = max(opts)
    # This finishes the computation
    stolen_item_ids = []
    weight_remaining = W
    while weight_remaining >= 0:
        item_id = S[weight_remaining]
        if item_id >= 0:
            stolen_item_ids.append('Steal Item ID %d: weight = %d, value = %f' % (item_id, weights[item_id], values[item_id]) )
            weight_remaining = weight_remaining - weights[item_id]
        else:
            break
    return T[W], stolen_item_ids




print(maxSteal_memo(25, weights, values))
print(maxSteal_memo(W, weights, values))