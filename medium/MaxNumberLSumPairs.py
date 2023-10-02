class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        d = {}

        for num in nums:
            diff =  k - num
            if num in d and d[num] > 0:
                ans += 1
                d[num] -= 1
            elif num <= k and diff not in d:
                d[diff] = 1
            elif num <= k and diff in d:
                d[diff] += 1

        return ans
