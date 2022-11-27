def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        i = step -1
        
        while i >=0 and array[i]>key:
            array[i+1] = array[i]
            i = i -1
       
        array[i+1] = key

a = [10,9,8,7]
insertionSort(a)
print(a)
        