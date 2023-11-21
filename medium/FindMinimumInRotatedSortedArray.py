class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = float('inf')

        while l <= r:
            curr = (l+r)//2
            res = min(res,nums[curr])
            if nums[curr] < nums[r]:
                r = curr - 1
            else:
                l = curr + 1
        
        return res
