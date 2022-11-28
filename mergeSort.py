def merge(array, left, mid, right):
    i = left
    j = mid + 1

    output_list = []
    while (i <= mid or j <=right):
        if(i <= mid and j <= right):
            if(array[i]< array[j]):
                output_list.append(array[i])
                i = i + 1
            else:
                output_list.append(array[j])
                j = j+1
        elif(i <= mid):
            output_list.append(array[i])
            i = i+1
        else:
            output_list.append(array[j])
            j = j+1
        
    for k in range(left, right+1):
        array[k] = output_list[k -left]
    
    return
        

def mergeSort(array, left, right):
    if(left== right):
        return
    elif(left + 1 == right):
        if(array[left]> array[right]):
            array[left], array[right] = array[right], array[left]
            
    else:
        mid = (left + right) //2
        mergeSort(array, left, mid)
        mergeSort(array, mid + 1, right)

        merge(array, left, mid, right)

a = [2,5,8,3,6,9,1,4,7,10]

mergeSort(a, 0, len(a)-1)
print(a)