class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        curr = end // 2
        while start <= end:
            if nums[curr] == target:
                return curr
            elif nums[curr] < target:
                start = curr + 1
                curr += 1
                curr = (curr + end) // 2
            else:
                end = curr - 1
                curr -= 1
                curr = (curr - start) // 2
        return -1
