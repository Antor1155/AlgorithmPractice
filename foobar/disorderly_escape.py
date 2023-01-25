# took inspiration form online while implementing the process of 
# burnside's lemma to account symmetry to deduct the duplicate combination
# with out the row- column shift rule, its just s^ (w * h) or total combinations.
# to calculate , find repeating grid pattern, deduct them and try next combination.
from math import factorial
from collections import Counter
from fractions import gcd

def c_count(c, n):
    c_c=factorial(n)
    for a, b in Counter(c).items():
        c_c//=(a**b)*factorial(b)
    return c_c        

def partitions(n, i=1):
    yield [n]
    for i in range(i, n//2 + 1):
        for p in partitions(n-i, i):
            yield [i] + p

def solution(w, h, s):    
    grid=0
    for cp_of_w in partitions(w):
        for cp_of_h in partitions(h):            
            m=c_count(cp_of_w, w)*c_count(cp_of_h, h)
            k = 0
            for j in cp_of_h:
                for i in cp_of_w:
                    k += gcd(i, j)

            grid += m *(s**k)
              
    return str(grid//(factorial(w)*factorial(h)))

print(solution(2, 2, 2))