class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        j = 0
        c_sum = 0

        for i, num in enumerate(nums):
            c_sum += num
            while c_sum >= target and j < len(nums):
                res = min(res,(i-j)+1)
                c_sum -= nums[j]
                j += 1
             
        return res if res < float('inf') else 0
