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


def qs_on_cm_first(l, start):
    sec_start= start
    sec_ends = start
    for i in range(start + 1, len(l)):
        if l[i][0] == l[start][0]:
            sec_ends += 1
        else:
            break
    if sec_start != sec_ends:
        quicksort(l,sec_start, sec_ends,1 )
    if sec_ends < len(l)-1:
        qs_on_cm_first(l, sec_ends+1)
    else:
        return

def final_qs(l, start):
    start= start
    end = start
    for i in range(start + 1, len(l)):
        if l[i][0] == l[start][0] and l[i][1] == l[start][1]:
            end += 1
        else:
            break
    if start != end:
        quicksort(l,start, end, 2 )
    if end < len(l)-1:
        final_qs(l, end+1)
    else:
        return

def convertBack(l):
    for i in range(len(l)):
        if l[i][1] == -1:
            l[i].pop()
            l[i].pop()
        elif l[i][2] == -1:
            l[i].pop()
        
        if len(l[i]) == 1:
            l[i] = str(l[i][0])
        elif len(l[i]) == 2:
            l[i] = str(l[i][0]) + "." + str(l[i][1])
        else:
            l[i] = str(l[i][0]) + "." + str(l[i][1]) + "." + str(l[i][2])
        


def solution(l):
    converter(l)
        
            
    quicksort(l, 0, len(l)-1, 0)
    # fixed to do 
    qs_on_cm_first(l, 0)
    # fixed to do at second level 
    final_qs(l, 0)

    convertBack(l)
    print(l)

l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]

solution(l)