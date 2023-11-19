class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            curr = (left + right) // 2
            if nums[curr] == target:
                return curr
            if nums[left] <= nums[curr]:
                if nums[left] <= target < nums[curr]:
                    right = curr - 1
                else:
                    left = curr + 1
            else:
                if nums[curr] < target <= nums[right]:
                    left = curr + 1
                else:
                    right = curr - 1
        return -1
