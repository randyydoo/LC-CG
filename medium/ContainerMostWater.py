#two pointer
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1
        while left <= right:
            max_height = min(height[left],height[right])
            distance = index(right) - index(left)
            area = max_height * distance
            if area > res:
                res = area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return re
