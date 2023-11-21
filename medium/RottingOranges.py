class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = -1
        q = collections.deque()
        r_len, c_len = len(grid), len(grid[0])
        s = set()

        for i in range(r_len):
            for j in range(c_len):
                if grid[i][j] == 2:
                    q.append([i,j])
                if grid[i][j] == 1:
                    s.add((i,j))
        if not s:
            return 0
            
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if (r+1, c) in s:
                    grid[r+1][c] = 2
                    q.append([r+1,c])
                    s.remove((r+1,c))
                if (r-1, c) in s: 
                    grid[r-1][c] = 2
                    q.append([r-1,c])
                    s.remove((r-1,c))
                if (r, c+1) in s: 
                    grid[r][c+1] = 2
                    q.append([r,c+1])
                    s.remove((r,c+1))
                if (r, c-1) in s:  
                    grid[r][c-1] = 2
                    q.append([r,c-1])
                    s.remove((r,c-1))
            res += 1
        return res if not s else -1
