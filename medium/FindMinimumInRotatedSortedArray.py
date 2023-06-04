class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        ans = nums[0]
        while left <= right:
            curr = (left + right) // 2
            if ans <= nums[curr]:
                left = curr + 1
            else:
                ans = nums[curr]
                right = curr - 1
        return ans
