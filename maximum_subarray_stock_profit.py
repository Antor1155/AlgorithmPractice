a = [ -4, 5, -6, 3, 5, 2, -4, 4, 15, 5, 20]

def max_profit(list, i, j):
    # print(list[i:j+1])
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


# doing the same thing with complexity 0(n)

def maxSubArray(a):
    n = len(a)
    if n == 1:
        return 0
    # your code here
    min = float("inf")
    maximum = 0
    for i in a:
        if i < min:
            min = i
        if i - min > maximum:
            maximum = i - min
    
    return maximum
        

print(maxSubArray(a))
        