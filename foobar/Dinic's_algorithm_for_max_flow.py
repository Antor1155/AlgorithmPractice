#Dinic Algorithm
def modify_path(path, start, ends):
    
    for i in range(1,len(start)):
        for ind, val in enumerate(path[start[i]]):
            path[0][ind] += val
    
    # path = path[:ends[0]+1]

    for i in range(len(path)):
        for j in range(1, len(ends)):
            k = path[i][ends[0]]
            l = path[i][ends[j]]
            path[i][ends[0]] += path[i][ends[j]]
            path[i][ends[j]] = 0
    return path

#build level graph by using BFS
def Bfs(C, F, s, t):  # C is the capacity matrix
        n = len(C)
        queue = []
        queue.append(s)
        global level
        level = n * [0]  # initialization
        level[s] = 1  
        while queue:
            k = queue.pop(0)
            for i in range(n):
                    if (F[k][i] < C[k][i]) and (level[i] == 0): # not visited
                            level[i] = level[k] + 1
                            queue.append(i)
        return level[t] > 0

#search augmenting path by using DFS
def Dfs(C, F, k, cp):
        tmp = cp
        if k == len(C)-1:
            return cp
        for i in range(len(C)):
            if (level[i] == level[k] + 1) and (F[k][i] < C[k][i]):
                f = Dfs(C,F,i,min(tmp,C[k][i] - F[k][i]))
                F[k][i] = F[k][i] + f
                F[i][k] = F[i][k] - f
                tmp = tmp - f
        return cp - tmp

#calculate max flow
#_ = float('inf')
def MaxFlow(C,s,t):
        n = len(C)
        F = [n*[0] for i in range(n)] # F is the flow matrix
        flow = 0
        while(Bfs(C,F,s,t)):
            print("while running")
            flow = flow + Dfs(C,F,s,2000000)
        return flow

#-------------------------------------
# make a capacity graph
# node   s   o   p   q   r   t
# C = [[ 0, 0, 4, 6, 0, 0 ],  # s
#      [ 0, 0, 2, 3, 0, 0 ],  # o
#      [ 0, 0, 0, 0, 2, 0 ],  # p
#      [ 0, 0, 0, 0, 4, 2 ],  # q
#      [ 0, 0, 0, 0, 0, 2 ],  # r
#      [ 0, 0, 0, 0, 0, 3 ]]  # t
path = [
  [0, 0, 4, 6, 0, 52],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 5],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]
C = [[0, 0, 9, 8, 0, 0],  # Room 0: Bunnies
     [0, 0, 9, 8, 0, 0],  # Room 1: Bunnies
     [0, 0, 0, 0, 8, 8],  # Room 2: Intermediate room
     [0, 0, 0, 0, 12, 12],  # Room 3: Intermediate room
     [5, 0, 0, 0, 5, 1]]  # Room 4: Escape pods]  # Room 5: Escape pods

source =  [0, 1]  # A
sink = [4, 5]   # F
path = modify_path(path, source, sink)
print( "Dinic's Algorithm")
print("path is", path)
max_flow_value = MaxFlow(path, source[0], sink[0])
# print ("max_flow_value is", max_flow_value)
