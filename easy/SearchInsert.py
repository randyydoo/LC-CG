class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums) - 1
        i = 0
        while i <= length:
            if i == length and nums[i] < target:
                return i + 1
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
            i += 1
        return 0
     

