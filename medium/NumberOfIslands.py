class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r_len, c_len = len(grid[0]), len(grid)
        c = 0

        def dfs(i, j,row_length, col_length):
            if i < 0 or i > col_length or j < 0 or j > row_length or grid[i][j] != '1':
                return 

            elif grid[i][j] == '1':
                print(i,j)
                grid[i][j] = '!'
            
            down = dfs(i+1, j, row_length, col_length)
            right = dfs(i, j+1, row_length, col_length)
            up = dfs(i-1, j, row_length, col_length)
            left = dfs(i, j-1, row_length, col_length)

            return 
         
        for i in range(c_len):
            for j in range(r_len):
                if grid[i][j] == '1':
                    dfs(i,j,r_len-1,c_len-1)
                    c += 1

        return c
