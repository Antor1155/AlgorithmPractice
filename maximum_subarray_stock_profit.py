a = [ -4, 5, -6, 3, 5, 2, -4, 20]

def max_profit(list, i, j):
    if i == j:
        return 0
    if i + 1 == j:
        return max(a[j] - a[i], 0)
    
    m = (i+j) //2 

    m1 = max_profit(list, i, m)
    m2 = max_profit(list, m+1, j)

    first_half = min(list[i: m+1])
    second_half = max(list[m+1 : j+1])

    return max(m1, m2, second_half - first_half)


print(max_profit(a, 0, len(a)-1))