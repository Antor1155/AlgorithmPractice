def bubbleDown(lst , i):
    left =  i * 2 + 1
    right = i * 2 + 2

    if(left >= len(lst)):
        return
    elif(left < len(lst) and right>=len(lst)):
        if(lst[left] < lst[i]):
            lst[left], lst[i] = lst[i], lst[left]
        return
    else:
        if(lst[left] < lst[right]):
            small = left
        else:
            small = right
        
        if(lst[small]< lst[i]):
            lst[small] , lst[i] = lst[i], lst[small]
            bubbleDown(lst, small)



a = [10, 20, 50, 30, 80, 60,70]
b = [30, 10, 50, 20, 80, 60,70]

bubbleDown(b, 0)
assert b == a, "test failed" 
print('\nbubble-down passed\n')


def minHeap(array):
    mid = len(array)//2

    while mid>= 0:
        bubbleDown(array, mid)
        mid = mid -1

k = [4, 2, 6, 2, 6, 20, 1, 5]

minHeap(k)

print(k)

