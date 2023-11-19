# BFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target = image[sr][sc]
        r_len, c_len = len(image), len(image[0])
        q, visited = collections.deque([(sr,sc)]), set()

        while q:
            i, j = q.popleft()
            visited.add((i,j))

            image[i][j] = color

            dirs = [[0,1], [1,0], [0,-1], [-1,0]]
            for x, y in dirs:
                if 0 <= i+x < r_len and 0 <= j+y < c_len and image[i+x][j+y] == target and (i+x, j+y) not in visited:
                    q.append((i+x, j+y))

        return image


# DFS
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
