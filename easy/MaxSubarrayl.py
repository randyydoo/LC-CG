class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp_sum = 0

        for i in range(k):
            temp_sum += nums[i]

        max_sum = temp_sum
        for j in range(k, len(nums)):
            temp_sum += nums[j] - nums[j-k]
            max_sum = max(max_sum,temp_sum)

        return max_sum/k
