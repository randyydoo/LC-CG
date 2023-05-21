def solve(board):
    dic = {"row": [[] for i in range(9)], "col" : [[] for i in range(9)], 'board': [[] for i in range(9)]}
    boardNum = 0
    row, col = 0, 0
    for i in range(len(board)):
        for j in range(len(board)):
            num = board[i][j]
            #figure out algo for updating board number using row and col
            if num in dic['row'][i] or num in dic['col'][j] or num in dic['board'][boardNum]:
                return False
            else:
                dic['row'][i].append(num)
                dic['col'][j].append(num)
                dic['board'][boardNum].append(num)
            col += 1
        row += 1
    return True


b=[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["20",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(solve(b))
