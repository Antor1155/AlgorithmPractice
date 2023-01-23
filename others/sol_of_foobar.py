#Dinic Algorithm
def modify_path(path, start, ends):
    
    for i in range(1,len(start)):
        for ind, val in enumerate(path[start[i]]):
            path[0][ind] += val
    
    path = path[:ends[0]+1]

    for i in range(len(path)):
        for j in range(1, len(ends)):
            path[i][ends[0]] += path[i][ends[j]]
    
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
            flow = flow + Dfs(C,F,s,2000001)
        return flow



def solution(entrances, exits, path):
    # Your code here
    path = modify_path(path, entrances, exits)
    
    return MaxFlow(path, entrances[0], exits[0])

print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))


print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))