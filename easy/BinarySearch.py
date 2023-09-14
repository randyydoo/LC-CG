class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        curr = (left + right)//2

        while left <= right:
            if nums[curr] == target:
                return curr
            elif nums[curr] < target:
                left = curr + 1
            elif nums[curr] > target:
                right = curr - 1

            curr = (right + left)//2
            
        return -1
