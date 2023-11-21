class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        new = sorted(nums)
        ans = 0
        temp = 1
        for i in range(1, len(new)):
            if new[i] - new[i - 1] == 1:
                temp += 1
            if temp > ans:
                ans = temp 
            if new[i] - new[i - 1] > 1:
                temp = 1
        return ans

