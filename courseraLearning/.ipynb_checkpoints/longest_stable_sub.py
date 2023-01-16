# longest stabel sub sequence of a list with difference of abs 1 , dsa course last--2nd week 
def computeLSS(a):
    # your code here
   
    n = len(a)
    
    length = [0] * n
    pre = [0] * n
    
    
    for i in range(n):
        max_j_length = 0
        max_j = None
        
        for j in range(i + 1):    
            if abs(a[j] - a[i]) <=1:
                if length[j] + 1 > max_j_length:
                    max_j_length = length[j] + 1
                    max_j = j
                
        length[i] = max_j_length
        pre[i] = max_j
        
    
    print("pre and length are: \n", length, '\n', pre)
    max_list_ends_with = length.index(max(length)) 
    
    sub = []
    print(max_list_ends_with)
    
    while True:
        sub.insert(0, a[max_list_ends_with])
        
        if pre[max_list_ends_with] == max_list_ends_with:
            return sub
        
        max_list_ends_with = pre[max_list_ends_with]
        
        

## BEGIN TESTS 
def checkSubsequence(a, b):
    i = 0
    j = 0
    n = len(a)
    m = len(b)
    for j in range(m-1):
        assert abs(b[j] - b[j+1]) <= 1
    while (i < n and j < m):
        if a[i] == b[j]: 
            j = j + 1
        i = i + 1
    if j < m:
        return False
    return True 

print('--Test 1 --')
a1 = [1, 4, 2, -2, 0, -1, 2, 3]
print(a1)
sub1 = computeLSS(a1)
print(f'sub1 = {sub1}')
assert len(sub1) == 4, f'Subsequence does not have length 4'
assert checkSubsequence(a1, sub1), f'Your solution is not a subsequence of the original sequence'

print('--Test2--')
a2 = [1, 2, 3, 4, 0, 1, -1, -2, -3, -4, 5, -5, -6]
print(a2)
sub2 = computeLSS(a2)
print(f'sub2 = {sub2}')
assert len(sub2) == 8
assert checkSubsequence(a2, sub2)