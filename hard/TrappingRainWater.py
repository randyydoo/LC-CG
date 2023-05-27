class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        i, j= 0, len(height) - 1
        left_max, right_max = 0, 0
        while i < j: 
            if height[i] > left_max:
                left_max = height[i]
            if height[j] > right_max:
                right_max = height[j]
            if left_max < right_max: 
                ans += left_max - height[i]
                i += 1
            else:
                ans += right_max - height[j]
                j -= 1
        return ans
