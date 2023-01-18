
from collections import deque
# modify array being safe in try function 
def safe_mod(array, h, w, q, d):
    try:
        # up 
        if array[h-1][w] == 0 and h-1 > -1:
            array[h-1][w] = [h, w, d]
            q.append([h-1, w, d])
    except:
        pass

    try:
        # down 
        if array[h+1][w] == 0:
            array[h+1][w] = [h, w, d]
            q.append([h+1, w, d])
    except:
        pass

    try:
        # left
        if array[h][w-1] == 0 and w-1 > -1:
            array[h][w-1] =[h, w, d]
            q.append([h, w -1, d])
    except:
        pass

    try:
        # right 
        if array[h][w+1] == 0:
            array[h][w+1] = [h, w, d]
            q.append([h, w +1, d])
    except:
        pass

# ***************safe mod from end **************************


# ****************************************
def safe_check(array,h, w, present_d):
    # --- solved:::: safe_check bug where h-2 or w-2 were checking last elemetn of list  -1 or -2 **** h-1 also can cause same problem 
    # --solved :: checking all four values and returing the best one i am not checking all four values, if one pass, then just returning it
    # didn't raise any unexpected errors while verify 
    updated_d = present_d
    try:
        # up 2 step
        if array[h-1][w] == 1 and h-1 > -1:
            if  array[h-2][w][2] > 0 and h -2 > -1:
                tem = array[h-2][w][2] + 1 +  abs(array[h][w][2])
                if updated_d > tem :
                    updated_d = tem
    except:
        pass

    # two sides of up is upper corner 
    try:
        # up left 1step
        if array[h-1][w] == 1 and h-1 > -1:
            if array[h-1][w-1][2] > 0 and w-1 > -1:
                tem = array[h-1][w-1][2] + 1 + abs(array[h][w][2])
                if updated_d > tem :
                    updated_d = tem
    except:
        pass
    try:
        # up right 1 step
        if array[h-1][w] == 1 and h-1 > -1:
            if array[h-1][w+1][2] > 0:
                tem = array[h-1][w+1][2] + 1 + abs(array[h][w][2])
                if updated_d > tem :
                    updated_d = tem
    except:
        pass


    try:
        # down 2 step
        if array[h+1][w] == 1:
            if array[h+2][w][2] > 0:
                tem = array[h+2][w][2] + 1 + abs(array[h][w][2])
                if updated_d > tem :
                    updated_d = tem
    except:
        pass

    # two sides of down is below corner 
    try:
        # below left
        if array[h+1][w] == 1:
            if array[h+1][w-1][2] > 0 and w-1 > -1:
                tem = array[h+1][w-1][2] + 1 + abs(array[h][w][2])
                if updated_d > tem :
                    updated_d = tem
    except:
        pass
    try:
        # below right
        if array[h+1][w] == 1:
            if array[h+1][w+1][2] > 0:
                tem = array[h+1][w+1][2] + 1 + abs(array[h][w][2])
                if updated_d > tem :
                    updated_d = tem
    except:
        pass


    try:
        # left
        if array[h][w -1] == 1 and w -1 > -1:
            if array[h][w-2][2] > 0 and w-2 > -1:
                tem = array[h][w-2][2] + 1 + abs(array[h][w][2])
                if updated_d > tem :
                    updated_d = tem
    except:
        pass

    try:
        # right 
        if array[h][w +1] == 1:
            if array[h][w+2][2] > 0:
                tem = array[h][w+2][2] + 1 + abs(array[h][w][2])
                if updated_d > tem :
                    updated_d = tem
    except:
        pass
    
    return (False, None) if updated_d == present_d else(True, updated_d)



def safe_mod_from_end(array, h, w, q, d, previous_distance):

    try:
        # up 
        if array[h-1][w][2] > 0 and h-1 > -1:
            array[h-1][w] = [h, w, d]
            q.append([h-1, w, d])
    except:
        pass

    try:
        # down 
        if array[h+1][w][2] > 0:
            array[h+1][w] = [h, w, d]
            q.append([h+1, w, d])
    except:
        pass

    try:
        # left
        if array[h][w-1][2] > 0 and w-1 > -1:
            array[h][w-1] =[h, w, d]
            q.append([h, w -1, d])
    except:
        pass

    try:
        # right 
        if array[h][w+1][2] > 0:
            array[h][w+1] = [h, w, d]
            q.append([h, w +1, d])
    except:
        pass

    return safe_check(array, h, w, previous_distance)










def solution(map):
    # Your code here
    q = deque()
    map[0][0] = [0, 0, 1]
    q.append([0, 0, 1])

    while q:
        h, w, d= q.popleft()
        safe_mod(map, h, w, q, d+1)
    
    # **************************************this part fixed **********************
    present_d = map[len(map)-1][len(map[0])-1][2]

    map[len(map)-1][len(map[0])-1] = [len(map)-1, len(map[0])-1, -1]
    q.append([len(map)-1, len(map[0])-1, -1])
    while q:
        h, w, d = q.popleft()
        

        succed, updated_distance = safe_mod_from_end(map, h, w, q, d-1, present_d)
        if succed:
            if updated_distance < present_d:
                present_d = updated_distance


    return present_d

