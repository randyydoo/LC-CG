class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        memo = [[0]*n for _ in range(m)]

        def dfs(i, j):
            if memo[i][j]:
                return memo[i][j]

            dirs = [[0, 1], [1,0], [0,-1], [-1,0]]
            c = 1
            for x, y in dirs:
                if 0 <= i+x < m and 0 <= j+y < n and matrix[i+x][j+y] > matrix[i][j]:
                    c = max(c, 1 + dfs(i+x, j+y))
            memo[i][j] = c

            return c

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res = max(res,dfs(i,j))

        return res
