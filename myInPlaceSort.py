# a = [13, 12, 10, 9, 4, 5, 8, 12, 3, 5, 7, 4, 3, 6, 4, 3, 7, 4, 53, 2 ,3, 5, 3]

a=[]
n=100
k = 0
import random
for i in range(n):
    a.append(random.randint(0,n))

print("generated random a with ele: ",len(a))

b = a.copy()
for x in range (len(a)//2):
    for i in range(0, len(a)):
        if(i+1 < len(a) and a[i]> a[i+1]):
            a[i], a[i+1] = a[i+1], a[i]
        if(i+2 <len(a) and a[i]> a[i+2]):
            a[i+1], a[i+2] = a[i+2] , a[i+1]
            a[i], a[i+1] = a[i+1], a[i]
        k = k +1

print("sorted random a")

print(len(a), len(a)//2)
list.sort(b)
print("took total steps:",k, "while n square is: ", len(a)* len(a), "\n while the difference is :", len(a) * len(a) -k)

if( a ==b):
    print("passed")
else:
    print("failed")