class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        r_max, c_max = len(grid), len(grid[0])
        def dfs(c, i, j, r_max, c_max):
            nonlocal res

            if i < 0 or i >= r_max or j < 0 or j >= c_max or grid[i][j] == 0:
                return
            
            c[0] += 1
            grid[i][j] = 0
            right = dfs(c, i, j+1, r_max, c_max)
            down = dfs(c, i+1, j, r_max, c_max)
            left = dfs(c, i, j-1, r_max, c_max)
            up = dfs(c, i-1, j, r_max, c_max)
            res = max(res,c[0])
        
        for i in range(r_max):
            for j in range(c_max):
                if grid[i][j] == 1:
                    dfs([0],i,j,r_max,c_max)

        return res
