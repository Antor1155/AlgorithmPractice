def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        i = step -1
        while i >=0 and array[i]>key:
            array[i+1] = array[i]
            i = i -1
            
        array[i+1] = key

a = [10,9,8,7,6,5,4,3,2,5,1,4,7,5,8]
insertionSort(a)
print(a)
        