def merge(array, left, mid, right):
    i = left
    j = mid + 1


    tmp_array=[]
    while(i <= mid or j <= right):
        if(i<=mid and j<=right):
            if(array[i]> array[j]):
                tmp_array.append(array[j])
                j = j+1
            else:
                tmp_array.append(array[i])
                i = i+1
        elif(i <= mid):
            tmp_array.append(array[i])
            i = i+1
        else:
            tmp_array.append(array[j])
            j = j +1
    
    for k in range(left, right+1):
        array[k] = tmp_array[k -left]
    return


def mergeSortHelper(array, left, right):
    if(left == right):
        return
    elif(left + 1 == right):
        if(array[left] > array[right]):
            array[left], array[right] = array[right], array[left]
        return
    else:
        mid = (left + right)//2
        mergeSortHelper(array, left, mid)
        mergeSortHelper(array, mid+1, right)
        merge(array, left, mid, right)





def mergeSort(array):
    if(len(array)<=1):
        return
    else:
        mergeSortHelper(array, 0, len(array)-1)

a = [2, 55, 8]

mergeSort(a)
print(a)