class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        while left <= right:
            length = min(height[left],height[right])
            width = right - left
            area = length * width
            if area > ans:
                ans = area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return ans
