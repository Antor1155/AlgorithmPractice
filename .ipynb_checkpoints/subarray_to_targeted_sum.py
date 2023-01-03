# A given list, whose which subarray comes most closest to a given target. 

# Code up the recurrence below which return the difference of closest summed subarray form the target.

def targetSum(S, i,  tgt):
    # your code here
    
    if tgt < 0:
        return 10000
    elif i >= len(S):
        return tgt
    else:
        return min(targetSum(S, i+1, tgt - S[i]) , targetSum(S, i+1, tgt))


def tgtSum(tgt, S):
    return targetSum(S, 0, tgt)

t1 = tgtSum(15, [1, 2, 3, 4, 5, 10]) # Should be zero
assert t1 == 0, 'Test 1 failed'

t2 = tgtSum(26, [1, 2, 3, 4, 5, 10]) # should be 1
assert t2 == 1, 'Test 2 failed'

t3 = (tgtSum(23, [1, 2, 3, 4, 5, 10])) # should be 0
assert t3 == 0, 'Test 3 failed'


t4 = (tgtSum(18, [1, 2, 3, 4, 5, 10])) # should be 0
assert t4 == 0, 'Test 4 failed'

t5 = (tgtSum(9, [1, 2, 3, 4, 5, 10])) # should be 0
assert t5 == 0, 'Test 5 failed'

t6 = (tgtSum(457, [11, 23, 37, 48, 94, 152, 230, 312, 339, 413])) # should be 1
assert t6 == 1, 'Test 6 failed'

t7 = (tgtSum(512, [11, 23, 37, 48, 94, 152, 230, 312, 339, 413])) # should be 0
assert t7 == 0, 'Test 7 failed'

t8 = (tgtSum(616, [11, 23, 37, 48, 94, 152, 230, 312, 339, 413])) # should be 1
assert t8 == 1, 'Test 8 failed'

print('All tests passed (10 points)!')




# list made up the closest to target 

def getBestTargetSum(S, tgt):
    l = len(S)
    assert tgt >= 0
    # your code here    
    new_tgt = tgt 

    sub = []
    
    subset =([[False for i in range(new_tgt + 1)] for i in range(len(S) + 1)])
                

    
# A Dynamic Programming solution for subset sum problem
# Returns true if there is a subset of 
# set[] with sun equal to given sum 
  
# Returns true if there is a subset of set[] 
# with sun equal to given sum
    def isSubsetSum(set, n, sum):

        # The value of subset[i][j] will be 
        # true if there is a
        # subset of set[0..j-1] with sum equal to i
        
        # If sum is 0, then answer is true 
        for i in range(n + 1):
            subset[i][0] = True

            # If sum is not 0 and set is empty, 
            # then answer is false 
            for i in range(1, sum + 1):
                subset[0][i]= False

            # Fill the subset table in bottom up manner
            for i in range(1, n + 1):
                for j in range(1, sum + 1):
                    if j<set[i-1]:
                        subset[i][j] = subset[i-1][j]
                    if j>= set[i-1]:
                        subset[i][j] = (subset[i-1][j] or 
                                       subset[i - 1][j-set[i-1]])

            # uncomment this code to print table 
            # for i in range(n + 1):
            # for j in range(sum + 1):
            # print (subset[i][j], end =" ")
            # print()
        
    
    while True:
        
        isSubsetSum(S, len(S), new_tgt)
    
        if subset[len(S)][new_tgt] == False:
            new_tgt = new_tgt -1
        else:
            break
    
    def findSub(subset, i, j):
        if i <= 0 and j <= 0:
            return
        elif subset[i-1][j] == True:
            findSub(subset, i-1, j)
        elif i > 0:
            sub.insert(0, S[i-1])
            findSub(subset, i-1, j- S[i-1])
            
    findSub(subset, len(S), new_tgt)
    
    return sub





def checkTgtSumRes(a, tgt,expected):
    a = sorted(a)
    res = getBestTargetSum(a, tgt)
    res = sorted(res)
    print('Your result:' , res)
    assert tgt - sum(res)  == expected, f'Your code returns result that sums up to {sum(res)}, expected was {expected}'
    i = 0
    j = 0
    n = len(a)
    m = len(res)
    while (i < n and j < m):
        if a[i] == res[j]: 
            j = j + 1
        i = i + 1
    assert j == m, 'Your result  {res} is not a subset of {a}'


print('--test 1--')
a1 = [1, 2, 3, 4, 5, 10]
print(a1, 15)
checkTgtSumRes(a1, 15, 0)

print('--test 2--')
a2 = [1, 8, 3, 4, 5, 12]
print(a2, 26)
checkTgtSumRes(a2, 26, 0)

print('--test 3--')
a3 = [8, 3, 2, 4, 5, 7, 12]
print(a3, 38)
checkTgtSumRes(a3, 38, 0)

print('--test 4 --')
a4 = sorted([1, 10, 19, 18, 12, 11, 0, 9,  16, 17, 2, 7, 14, 29, 38, 45, 13, 26, 51, 82, 111, 124, 135, 189])
print(a4)
checkTgtSumRes(a4, 155, 0)
print('--test 5--')
checkTgtSumRes(a4, 189, 0)

print('--test 7--')
checkTgtSumRes(a4, 347, 0)

print('--test 8--')
checkTgtSumRes(a4, 461, 0)


print('--test 9--')
checkTgtSumRes(a4, 462, 0)


print('--test 9--')
checkTgtSumRes(a4, 517, 0)


print('--test 10--')
checkTgtSumRes(a4, 975, 3)

print('All Tests Passed (15 points)')

