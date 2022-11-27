
def insertionSort(array):
    for i in range(1, len(array)):
        ele = array[i]

        j = i-1
        while j >=0 and ele < array[j]:
            array[j+1] = array[j]
            j = j-1
        
        array[j+1] = ele 


def binarysearchHelper(array, ele, left, right):
    if(left > right):
        return False
    else:
        mid = (left + right)//2
        if(ele == array[mid]):
            return mid
        elif(ele<array[mid]):
            return binarysearchHelper(array, ele, left, mid-1)
        else:
            return binarysearchHelper(array, ele, mid +1, right)
        

def binarySearch(array, ele):
    if(ele < array[0] or ele > array[len(array)-1]):
        return False
    else:
        return binarysearchHelper(array, ele, 0, len(array)-1)


a = [5, 6, 3, 43, 45, 303, 33, 25, 2]
print(a)
insertionSort(a)
print("sorted a:", a)

k = binarySearch(a, 6)

print("ther required element is at position ",k)