
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
    # present_d = map[len(map)-1][len(map[0])-1][2]
    # current_at = [len(map)-1, len(map[0])-1]

    # while current_at != [0, 0, 1]:
    #     succed, updated_distance = safe_check(map, current_at[0], current_at[1], map[len(map)-1][len(map[0])-1][2])
    #     if succed:
    #         # this line of code passed test 3 ******************
    #         # before it was return and didn't pass test 3
    #         # so there can be multiple way which will produce better result.
    #         if updated_distance < present_d:
    #             print("updated d:",updated_distance, " current at: ", current_at)
    #             present_d = updated_distance
    #     current_at = map[current_at[0]][current_at[1]]

    # return present_d


# confution: if there any case where is no way to elcape...... 

# base1 ans = 7 
base1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# base2 ans = 11 
base2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# this case is for when no path connected need to bfs form end
# priority last 
# a = [[0, 0, 0, 0, 0, 0],
#      [1, 1, 1, 1, 1, 1],
#      [0, 0, 0, 0, 0, 0], 
#      [0, 1, 1, 1, 1, 1],
#      [0, 0, 0, 0, 1, 0],
#      [0, 1, 1, 1, 1, 1], 
#      [0, 0, 0, 0, 0, 0]]

# solved: priority 1 
# for corner case i didn't think of which may join conrer
# just need to change in safe check **********************
# ans = 11 
a = [[0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 0],
     [1, 0, 0, 0, 0, 0],
     [1, 0, 1, 1, 1, 1],
     [1, 0, 1, 1, 1, 1], 
     [1, 0, 0, 0, 0, 0]]

# solved: priority 2
# for another case where bfs for last elemetn may solve the question
# expected ans = 12
# a = [[0, 0, 0, 0, 0, 0],
#      [0, 1, 1, 1, 1, 0],
#      [0, 1, 1, 1, 1, 0], 
#      [1, 1, 1, 0, 0, 0],
#      [0, 1, 1, 0, 1, 1],
#      [0, 1, 1, 0, 1, 1], 
#      [0, 0, 0, 0, 0, 0]]

print("solution of a : " ,solution(a))
# solution(a)
for i in a:
    print(i)