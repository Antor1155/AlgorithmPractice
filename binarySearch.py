def binarySearchHelper(array, ele, left, right):
    if(left > right):
        return False
    else:
        mid = (left + right) //2

        if array[mid] == ele:
            return mid
        elif array[mid] < ele:
            return binarySearchHelper(array, ele, mid + 1, right)
        else:
            return binarySearchHelper(array, ele,left, mid -1 )


def binarySearch(array, ele):
    return binarySearchHelper(array, ele, 0, len(array)+1)


a = [1,3,5, 6, 7, 8, 19]
k = binarySearch(a, 1)

print("the element is at position",k)