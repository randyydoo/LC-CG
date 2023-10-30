class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix)-1
        l, r = 0, len(matrix[0])-1

        while i <= j:
            curr_row = i + ((j-i)//2)
            if matrix[curr_row][0] > target:
                j = curr_row-1
            elif matrix[curr_row][-1] < target:
                i = curr_row+1
            else:
                break

        while l <= r:
            curr = l + ((r-l)//2)
            if matrix[curr_row][curr] == target:
                return True
            elif matrix[curr_row][curr] > target:
                r = curr - 1
            elif matrix[curr_row][curr] < target:
                l = curr + 1 
        return False
