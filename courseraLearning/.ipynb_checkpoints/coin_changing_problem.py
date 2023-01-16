def minCoins_1(x, lst):
    T = [0] * (x+1) # memo table
    S = [-1]* (x+1) # best current/immediate decision
    coins_used = []
    for i in range(1,x+1):
        opts = [ (1 + T[i - cj], cj)  for cj in lst if i - cj >= 0]
        opts.append((1000000000, -1)) # Append + infinity to avoid min(..) raising an exception in the next line
        T[i], S[i] = min(opts)
    # NOW RECOVER the list of coins by using the S table.
    value_left = x
    while value_left > 0:
        coins_used.append(S[value_left])# append the immedidate decision
        value_left = value_left - S[value_left] # update the amount left
    assert value_left == 0
    return T[x], coins_used


lst0 = [1, 4, 7, 9, 16, 43]


print(minCoins_1(17, lst0))
print(minCoins_1(23, lst0))
# Compare the running time to the recursive version :-)
print(minCoins_1(35, lst0))
print(minCoins_1(298, lst0))