class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0 

        for num in nums:
            if num - 1 not in nums:
                c, temp = 1, num + 1
                while temp in nums:
                    c += 1
                    temp += 1
                res = max(c, res)

        return res
