def solution(a):
    rows, cols = len(a), len(a[0]) - 1
    #take transpose then swap [i][j] <-> [i][cols - j]
    for i in range(rows):
        for j in range(i):
           a[i][j], a[j][i] = a[j][i], a[i][j] 
    
    for i in range(rows):
        for j in range(len(a) // 2):
            a[i][j], a[i][cols - j] = a[i][cols - j], a[i][j]
            
    return a
