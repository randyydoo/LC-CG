class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i, j, target, visited):
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != target or (i,j) in visited:
                return

            visited.add((i,j)) 
            image[i][j] = color
            paths = [[0,1], [1,0], [0,-1], [-1,0]]
            for x, y in paths:
                dfs(i+x, j+y, target, visited)

            return image
        return dfs(sr,sc, image[sr][sc], set())
