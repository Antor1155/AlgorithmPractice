# third week assignment
# allocate works to n processors in a manner the max finish time of processors in the lowest 


# **************************************************
# this process don't privide the best ans and give answer within
#  range of (2- 1/m) of optimal solution 
#  where m is the number of processors. but as making all combination of 1000 numbers 
# in 10 processors in 10 ** 1000 which is even more than atoms in galaxy. so, here, even
# optimal solution is possible, we don't want it.
# this approach is for online when input in coming.


# but offline approach with sorted jobs in decending order (high to low) will give
#  the best ans .. all process same, with only the jobs are sorted then we use greed alg.all

#  ********************************************





def compute_makespan(times, m, assign):
    # times is an array of job times of size n
    # m is the number of processors
    # assign is an array of size n whose entries are between 0 to m-1 
    # indicating the processor number for
    # the corresponding job.
    # Return: makespan of the assignment
    # your code here
    
    span_array  = [0] * m 
    
    for i in range(len(assign)):
        span_array[assign[i]] = span_array[assign[i]] + times[i] 
    
    return max(span_array)


## BEGIN TESTS
print('Test 1 ... ', end = '')
times = [2, 2, 2, 2, 3, 3, 2]
assigns = [0, 0, 0, 0, 1, 1, 2]
m = 3
s = compute_makespan(times, m, assigns)
assert s == 8, f'Expected makespan is 8, your code returned: {s}'
print(' passed!')

print('Test 2 ...', end='')
times = [2, 1, 2, 2, 1, 3, 2, 1, 1, 3]
assigns = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
m = 3
s = compute_makespan(times, m, assigns)
assert s == 10, f' Expected makespan is 10, your code returned {s}'
print('  passed!')
print('Tests passed: 10 points!')




def greedy_makespan_min(times, m):
    # times is a list of n jobs.
    assert len(times) >= 1
    assert all(elt >= 0 for elt in times)
    assert m >= 2
    n = len(times)
    # please do not reorder the jobs in times or else tests will fail.
    # you can implement a priority queue if you would like.
    # use https://docs.python.org/3/library/heapq.html heapq data structure 
    # Return a tuple of two things: 
    #    - Assignment list of n numbers from 0 to m-1
    #    - The makespan of your assignment
    # your code here
    proces = [0] * m
    assign = [None] * n
    
    for i in range(n):
        min_proces = proces.index(min(proces))
        
        assign[i] = min_proces
        proces[min_proces] = proces[min_proces] + times[i]
        
    span = compute_makespan(times, m, assign)
    
    
    return (assign, span)
    



## BEGIN TESTS
def do_test(times, m, expected):
    (a, makespan) = greedy_makespan_min(times,m )
    print('\t Assignment returned: ', a)
    print('\t Claimed makespan: ', makespan)
    assert compute_makespan(times, m, a) == makespan, 'Assignment returned is not consistent with the reported makespan'
    assert makespan == expected, f'Expected makespan should be {expected}, your core returned {makespan}'
    print('Passed')
print('Test 1:')
times = [2, 2, 2, 2, 2, 2, 2, 2, 3] 
m = 3
expected = 7
do_test(times, m, expected)

print('Test 2:')
times = [1]*20 + [5]
m = 5
expected =9
do_test(times, m, expected)

print('Test 3:')
times = [1]*40 + [2]
m = 20
expected = 4
do_test(times, m, expected)
print('All tests passed: 15 points!')
## END TESTS