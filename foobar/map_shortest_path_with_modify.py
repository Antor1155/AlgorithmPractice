
from collections import deque
# modify list being safe in try function
# the array itself carry the weight and prent's position  
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



# this function check for adjacent wall and
# any path adjacent to the wall with which corrent path might connect
def safe_check(array,h, w, present_d):
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


# this function could be inserted in safe_mod function but it would look complicated
# this function used when start and end is connected but to find better way
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

    # bfs form start to end 
    while q:
        h, w, d= q.popleft()
        safe_mod(map, h, w, q, d+1)
    
    
    q.append([len(map)-1, len(map[0])-1, -1])
    present_d = (len(map)-1) * (len(map[0])-1)

    # to check if start and end is connected of not
    try:
        present_d = map[len(map)-1][len(map[0])-1][2]
    except:

        # if not connected bfs form end toward start while checkign any 1 step far path from start
        map[len(map)-1][len(map[0])-1] = [len(map)-1, len(map[0])-1, -1]
        while q:
            h, w, d= q.popleft()
            safe_mod(map, h, w, q, d-1)
            succed, updated_distance = safe_check(map, h, w, present_d)
            if succed:
                if updated_distance < present_d:
                    present_d = updated_distance
        
        return present_d

    # if try function succed , single bfs to find better path form end to start
    map[len(map)-1][len(map[0])-1] = [len(map)-1, len(map[0])-1, -1]

    while q:
        h, w, d = q.popleft()

        succed, updated_distance = safe_mod_from_end(map, h, w, q, d-1, present_d)
        if succed:
            if updated_distance < present_d:
                present_d = updated_distance


    return present_d





# confution: if there any case where is no way to elcape...... 

# base1 ans = 7 
base1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# base2 ans = 11 
base2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# this case is no path connected need to bfs form end
# priority last 
# result = 20
a4= [[0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 0, 0], 
     [0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 0],
     [0, 1, 1, 1, 1, 1], 
     [0, 0, 0, 0, 0, 0]]


# where multiple way form a to b:
# result = 14
a3 = [[0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 0, 1],
     [1, 1, 1, 1, 0, 0], 
     [0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 0],
     [0, 1, 1, 1, 1, 1], 
     [0, 0, 0, 0, 0, 0]]

# solved: priority 1 
# for corner case i didn't think of which may join conrer
# just need to change in safe check **********************
# ans = 11 
a2 = [[0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 0],
     [1, 0, 0, 0, 0, 0],
     [1, 0, 1, 1, 1, 1],
     [1, 0, 1, 1, 1, 1], 
     [1, 0, 0, 0, 0, 0]]

# solved: priority 2
# for another case where bfs for last elemetn may solve the question
# expected ans = 12
a1 = [[0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 1, 1, 1, 1, 0], 
     [1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 1],
     [0, 1, 1, 0, 1, 1], 
     [0, 0, 0, 0, 0, 0]]

print("12-- a1 bfs for end give new sol : " ,solution(a1))
print("11-- a2 corner case : " ,solution(a2))
print("14-- a3 multiple way start-end : " ,solution(a3))
print("20-- a4 start and end not connected : " ,solution(a4))
print("7 of base1 : " ,solution(base1))
print("11 of base1 : " ,solution(base2))
