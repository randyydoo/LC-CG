class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # stores all invalid regions 
        r, c = len(board)-1, len(board[0])-1
        bank = set()
        def dfs(i, j, visited):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == 'X' or (i, j) in visited:
                return
            visited.add((i,j)) 
            return dfs(i,j+1, visited) or dfs(i+1,j, visited) or dfs(i,j-1, visited) or dfs(i-1,j, visited) 

        for i in range(r+1):
            dfs(i, 0, bank)
            dfs(i, c, bank)

        for i in range(c+1):
            dfs(0, i, bank)
            dfs(r, i, bank)

        for i in range(r+1):
            for j in range(c+1):
                if (i, j) not in bank and board[i][j] == 'O':
                    board[i][j] = 'X'
