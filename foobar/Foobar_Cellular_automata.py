# This question belong to Cellular Automata and have to calculate possible t-1 prestates lead to current state 
# de Brujin diagram of preimages of a cell corrosponding to its neighbour cells inspired the solution. 

# took inspiration from differnt implementation techniques form internet and this approach was providing the 
# lowest memory usege, approx: 15.60  MiB for largest test case provided with question (used: memory_profiler) and 
# rum time 0.0019 s on R7 5800H processor which was also lowest among all other implementations.


from collections import defaultdict

def g_steps(c1,c2,bitlen):
    a = c1 & ~(1<<bitlen)
    b = c2 & ~(1<<bitlen)
    c = c1 >> 1
    d = c2 >> 1
    return (a&~b&~c&~d) | (~a&b&~c&~d) | (~a&~b&c&~d) | (~a&~b&~c&d)

def build_map(n, nums):
    g_map = defaultdict(set)
    nums = set(nums)
    for i in range(1<<(n+1)):
        for j in range(1<<(n+1)):
            steps = g_steps(i,j,n)
            if steps in nums:
                g_map[(steps, i)].add(j)
    return g_map

def solution(g):
    g = list(zip(*g)) # transpose
    num_cols = len(g[0])

    # turn map into numbers
    nums = []
    for row in g:
        sub_n = 0
        for i, col in enumerate(row):
            if col:
                sub_n += (1<< i)
        nums.append(sub_n)

    g_map = build_map(num_cols, nums)

    pre_state = {}
    for i in range(1<< num_cols + 1):
        pre_state[i] = 1

    for value in nums:
        final_v = defaultdict(int)
        for c1 in pre_state:
            for c2 in g_map[(value, c1)]:
                final_v[c2] += pre_state[c1]
        pre_state = final_v

    res = sum(pre_state.values())
    return res


a = [[True, True, False, True, False, True, False, True, True, False],
     [True, True, False, False, False, False, True, True, True, False], 
     [True, True, False, False, False, False, False, False, False, True], 
     [False, True, False, False, False, False, True, True, False, False]]

print(solution(a))


if __name__ == '__main__':
    solution(a)