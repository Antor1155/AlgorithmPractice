def quicksort(array, low, high, p):
    if low > high:
        return
    i = low
    pivot = array[high][p]
    for ind in range(low, high):
        if array[ind][p] < pivot:
            array[i], array[ind] = array[ind], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]  
    quicksort(array, low, i -1, p)
    quicksort(array, i + 1, high, p)

def converter(l):
    for i in range(len(l)):
        l[i] = l[i].split(".")
        for j in range(len(l[i])):
            l[i][j] = int(l[i][j])

        if len(l[i]) == 1:
            l[i].append(-1)
            l[i].append(-1)
        elif len(l[i]) == 2:
            l[i].append(-1)


def special_for_second(l, start):
    sec_start= start
    sec_ends = start
    for i in range(start + 1, len(l)):
        if l[i][0] == l[start][0]:
            sec_ends += 1
        else:
            break
    quicksort(l,sec_start, sec_ends,1 )
    if sec_ends < len(l)-1:
        special_for_second(l, sec_ends+1)
    else:
        return


def solution(l):
    converter(l)
        
            
    quicksort(l, 0, len(l)-1, 0)
    # fixed to do 
    special_for_second(l, 0)
    # quicksort(l, 1, 5, 1)
    # quicksort(l, 3, 4, 2)
    print(l)

l = ["1.11", "2.1.0","1", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]

solution(l)