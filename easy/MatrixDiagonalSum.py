class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        cols = len(mat)
        rows = len(mat[0]) - 1
        for i in range(len(mat)):
            if len(mat) % 2 is not 0 and rows - i is i:
                ans += mat[i][rows - i]
            else:
                ans += mat[i][i] + mat[i][rows - i]
        return ans
        #two pointer algo
        #ans = 0
        #end = len(mat) - 1
        #start = 0
        #if len(mat) == 1:
        #    return mat[0][0]
        #while start <= end:
        #    if len(mat) % 2 is not 0 and start == end:
        #        ans += mat[start][start]
        #        return ans
        #    else:
        #        ans += mat[start][start]
        #        ans += mat[start][end]
        #        ans += mat[end][start]
        #        ans += mat[end][end]
        #    start += 1
        #    end -= 1
        #return ans


