class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        right, bottom = len(matrix[0]) - 1, len(matrix) - 1
        left, top = 0, 0

        while len(ans) < len(matrix[0]) * len(matrix):
            #go right
            for i in range(left, right + 1):
                ans.append(matrix[left][i])
            top += 1
            
            #go down
            for j in range(top ,bottom + 1):
                ans.append(matrix[j][right])
            right -= 1

            if bottom >= top: 
            #go left
                for k in reversed(range(left, right + 1)):
                    ans.append(matrix[bottom][k])
                bottom -= 1

            #go up
            if right >= left:
                for l in reversed (range(top,bottom + 1)):
                    ans.append(matrix[l][left])
                left += 1
        return ans
