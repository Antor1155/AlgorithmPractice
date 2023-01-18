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

# ****************************************
def safe_check(array,h, w, present_d):
    try:
        # up 
        if array[h-1][w] == 1:
            if array[h][w][2] - array[h-2][w][2] > 2:
                present_d = array[h-2][w][2] + 2 + present_d - array[h][w][2]
                return True, present_d
    except:
        pass

    try:
        # down 
        if array[h+1][w] == 1:
            if array[h][w][2] - array[h+2][w][2] > 2:
                present_d = array[h+2][w][2] + 2 + present_d - array[h][w][2]
                return True, present_d
    except:
        pass

    try:
        # left
        if array[h][w -1] == 1:
            if array[h][w][2] - array[h][w-2][2] > 2:
                present_d = array[h][w-2][2] + 2 + present_d - array[h][w][2]
                return True, present_d
    except:
        pass

    try:
        # right 
        if array[h][w +1] == 1:
            if array[h][w][2] - array[h][w+2][2] > 2:
                present_d = array[h][w+2][2] + 2 + present_d - array[h][w][2]
                return True, present_d
    except:
        pass
    
    return False, None




def solution(map):
    # Your code here
        # Your code here
    q = deque()
    map[0][0] = [0, 0, 1]
    q.append([0, 0, 1])

    while q:
        h, w, d= q.popleft()
        safe_mod(map, h, w, q, d+1)
    
    # **************************************this part fixed **********************
    # testing case when the maze is not solved or end is not reached 
  
    # if not(map[len(map)-1][len(map[0])-1]):
    #     distance = 20 * 20
    #     map[len(map) -1][ len(map[0])-1] = [len(map)-1, len(map[0])-1, -1]
    #     # check upper one 
    #     q.append([len(map)-1, len(map[0])-1, -1])
    #     while q:
    #         h, w, d= q.popleft()

    #         succed, x = safe_check(map, h, w, d)
    #         if succed:
    #             if x < distance:
    #                 distance = x

            
    #         safe_mod(map, h, w, q, d-1)

    #     # return distance
    #     return distance





    # ********************************* this part fixed ****************************
    present_d = map[len(map)-1][len(map[0])-1][2]
    current_at = [len(map)-1, len(map[0])-1]

    while current_at != [0, 0, 1]:
        succed, updated_distance = safe_check(map, current_at[0], current_at[1], map[len(map)-1][len(map[0])-1][2])
        if succed:
            # this line of code passed test 3 ******************
            # before it was return and didn't pass test 3
            # so there can be multiple way which will produce better result.
            if updated_distance < present_d:
                present_d = updated_distance
        current_at = map[current_at[0]][current_at[1]]

    return present_d


# confution: if there any case where is no way to elcape...... 


# a = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# this case is for when no path connected 
# a = [[0, 0, 0, 0, 0, 0],
#      [1, 1, 1, 1, 1, 1],
#      [0, 0, 0, 0, 0, 0], 
#      [0, 1, 1, 1, 1, 1],

#      [0, 0, 0, 0, 1, 0],

#      [0, 1, 1, 1, 1, 1], 
#      [0, 0, 0, 0, 0, 0]]


# for corner case i didn't think of 
a = [[0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 1, 1, 1, 1, 0], 
     [1, 0, 0, 0, 0, 0],
     [1, 0, 1, 1, 1, 1],
     [1, 0, 1, 1, 1, 1], 
     [1, 0, 0, 0, 0, 0]]

print("solution is : " ,solution(a))
for i in a:
    print(i)