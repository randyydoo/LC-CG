class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic = {"row": [[] for i in range(9)], "col" : [[]  for i in range(9)], 'board': [[] for i in range(9)]}
        curr = 0
        for i in range(len(board)):
            temp = 0
            if i != 0 and i % 3 == 0:
                curr += 3
            for j in range(len(board)):
                num = board[i][j]
                if j != 0 and j % 3 == 0:
                    temp += 1
                if num == ".":
                    continue
                if num in dic['row'][i] or num in dic['col'][j] or num in dic['board'][curr + temp]:
                    return False
                else:
                    dic['col'][j].append(num)
                    dic['row'][i].append(num)
                    dic['board'][curr + temp].append(num)
        return True
