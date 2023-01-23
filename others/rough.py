def modify_path(path, start, ends):
    
    for i in range(1,len(start)):
        for ind, val in enumerate(path[start[i]]):
            path[0][ind] += val
    
    path = path[:ends[0]+1]

    for i in range(len(path)):
        for j in range(1, len(ends)):
            k = path[i][ends[0]]
            l = path[i][ends[j]]
            path[i][ends[0]] += path[i][ends[j]]
    
    print(path)



path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]

modify_path(path, [0, 1], [4, 5])

C = [[0, 0, 9, 8, 0, 0],  # Room 0: Bunnies
     [0, 0, 9, 8, 0, 0],  # Room 1: Bunnies
     [0, 0, 0, 0, 8, 8],  # Room 2: Intermediate room
     [0, 0, 0, 0, 12, 12],  # Room 3: Intermediate room
     [5, 0, 0, 0, 0, 1]]  # Room 4: Escape pods]  # Room 5: Escape pods