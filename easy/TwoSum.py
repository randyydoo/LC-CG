class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for i in range (0, len(nums)):
            key = target - nums[i]
            if key not in hMap:
                hMap[nums[i]] = i
            elif key in hMap:
                return hMap[key],i 
