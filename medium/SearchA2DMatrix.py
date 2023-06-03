class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1 and matrix[0][0] == target:
            return True
        for i in range(len(matrix)):
            curr = (len(matrix[i]) - 1) // 2
            left, right = 0, len(matrix[i]) - 1
            while left <= right:
                if matrix[i][curr] == target:
                    return True
                elif matrix[i][curr] < target:
                    left = curr + 1
                    curr += 1
                    curr += (right - left) // 2
                else:
                    right = curr - 1
                    curr -= 1
                    curr -= (right - left) // 2
        return False
