class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        rows, cols, valid = defaultdict(int), defaultdict(int), set()
        res = 0 
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    valid.add((i, j))
                    rows[i] += 1
                    cols[j] += 1
        
        for r, c in valid:
            if rows[r] + cols[c] == 2:
                res += 1
            
        return res
