#Let's memoize

def memoize_lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    # let's create a memo table and fill it with zeros. This will nicely take care of the base cases.
    memo_tbl = [ [0 for j in range(n+1)] for i in range(m+1)]
    sol_info = [ ['' for j in range(n+1)] for i in range(m+1)] # This will help us recover solutions
    for i in range(m-1, -1, -1): # iterate from m-1 to 0 with a step of -1
        for j in range(n-1, -1, -1):
            if s1[i] == s2[j]:
                memo_tbl[i][j] = memo_tbl[i+1][j+1] + 1
                sol_info[i][j] = 'match'
            else: 
                # Python allows us to compare and assign tuples
                # This nifty bit of code saves us an if then else condition and assignments
                # if you are new to python feel free to write out the logic carefully
                memo_tbl[i][j], sol_info[i][j] = max((memo_tbl[i+1][j],'right'), (memo_tbl[i][j+1], 'down'))
    # Now let us recover the longest common sub sequence
    lcs = '' # initialize it to empty string
    match_locations = [] # matches of (i,j)
    i = 0
    j = 0 # start at top left corner
    while (i < m and j < n):
        if sol_info[i][j] == 'match':
            assert s1[i] == s2[j]
            lcs = lcs + s1[i]
            match_locations.append((i,j))
            i,j = i + 1, j + 1
        elif sol_info[i][j] == 'right':
            i, j = i+1, j
        else: 
            assert sol_info[i][j] == 'down'
            i, j = i, j+1
    return lcs, match_locations



s1 = "GATTACA"
s2 = "ACTGATAACAA"
(lcs, match_locations) = memoize_lcs(s1, s2)
print(f'Longest common subsequence: {lcs} length= {len(lcs)}')
print('Matches:')
print('\t Char:\t i, j')
for (i, j) in match_locations:
    print(f'\t {s1[i]}:\t {i}, {j}')



s1 = "GGATTACCATTATGGAGGCGGA"
s2 = "ACTTAGGTAGG"
(lcs, match_locations) = memoize_lcs(s1, s2)
print(f'Longest common subsequence: {lcs} length= {len(lcs)}')
print('Matches:')
print('\t Char:\t i, j')
for (i, j) in match_locations:
    print(f'\t {s1[i]}:\t {i}, {j}')




#slightly longer strings will run instantaneously given that we are memoizing
s1 = "GGATTACACATTACCTATAGGTATAAT"
s2 = "GGATTTATCTATAAATTACCTATTTATTATATTACCGTATGGTATGC"
(lcs, match_locations) = memoize_lcs(s1, s2)
print(f'Longest common subsequence: {lcs} length= {len(lcs)}')
print('Matches:')
print('\t Char:\t i, j')
for (i, j) in match_locations:
    print(f'\t {s1[i]}:\t {i}, {j}')