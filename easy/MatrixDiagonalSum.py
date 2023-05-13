#2 pointer 
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        end = len(mat) - 1
        start = 0
        if len(mat) == 1:
            return mat[0][0]
        while start <= end:
            if len(mat) % 2 is not 0 and start == end:
                ans += mat[start][start]
                return ans
            else:
                ans += mat[start][start]
                ans += mat[start][end]
                ans += mat[end][start]
                ans += mat[end][end]
            start += 1
            end -= 1
        return ans


