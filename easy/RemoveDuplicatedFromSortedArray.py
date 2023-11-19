# Recrusion solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def helper(i, j, nums):
            if i == j or i >= len(nums) or j >= len(nums):
                return
            elif nums[j] == nums[i]:
                del nums[j]
                helper(i,j,nums)

            helper(j,j+1, nums)
            return nums
        
        helper(0,1, nums)
        return len(nums)

# 2 Pointer Solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[c] = nums[i]
                c += 1

        return c
