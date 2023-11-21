class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(i, j, prev, visited):
            if i < 0 or i >= rows or j < 0 or j >= cols or heights[i][j] < prev or (i,j) in visited:
                return
            visited.add((i,j))
            return dfs(i,j+1, heights[i][j], visited) or dfs(i+1,j, heights[i][j], visited) or dfs(i,j-1, heights[i][j], visited) or dfs(i-1,j, heights[i][j], visited)

        j = rows -1 
        for i in range(cols):
            dfs(0, i, heights[0][i], pac)
            dfs(j, i, heights[j][i], atl)
        j = cols - 1
        for i in range(rows):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, j, heights[i][j], atl)
        for cord in pac:
            if cord in atl:
                res.append([cord[0], cord[1]])
        return res
