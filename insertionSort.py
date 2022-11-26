def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]

        j = step - 1
        while j>=0 and key < array[j]:
            array[j+1] = array[j]
            array[j] = key 
            j = j-1

        array[j +1] = key


a = [10,9,8,7,6,5,4,3,2,5,1,4,7,5,8]
insertionSort(a)
print(a)
        