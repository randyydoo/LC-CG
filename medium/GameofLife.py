class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        ones = set()
        zeros =set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    ones.add((i,j))
                else:
                    zeros.add((i,j))
        
        neighs = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
        for i,j in zeros:
            c = 0
            for x,y in neighs:
                if 0 <= i+x < m and 0 <= j+y < n and (i+x, j+y) in ones:
                    c += 1
            if c == 3:
                board[i][j] = 1

        for i,j in ones:
            c = 0
            for x,y in neighs:
                if 0 <= i+x < m and 0 <= j+y < n and (i+x, j+y) in ones:
                    c += 1
            if c < 2 or c > 3:
                board[i][j] = 0

        return board
