# this question is about the beatty sequence where need to find addition of number while taking floor of multiplication with 
# irrational number: when s(ir, n),2 < ir (irrational nubmer) < 1 it produces one seq of number and 2 + ir produces another
# sequences of number thus we get the whole n elements in increasing order. 
# handeling beatty seq with square root of 2, with increasing order, found efficent formula form https://math.stackexchange.com/


from decimal import *
# deciaml class to handle ans upto precision of expected length as floating point number operation is not well precise.

def solution(s):
    getcontext().prec= 101
    sqof2 = Decimal(2).sqrt()
    
    def sol(a, n):
        nk = int((a - 1) * n)
        if n == 0:
            return 0

        return (n + nk) * (n + nk + 1) / 2 - nk * (nk + 1) - sol(a, nk)

# for number = n ^k :::runtime is::: (k log n / log(1/ sqrt(2) -1)  
    return str(int(sol(sqof2, int(s))))


print(solution("1234556789123455678912345567891234556789123455678912345567891234556789123455678912345567891234556789"))
# print(solution("5"))

# print(math.sqrt(2))
# getcontext().prec = 101
# print(Decimal(2).sqrt())