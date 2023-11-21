class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles)
        left, right = 1, max(piles) 
        while left <= right:
            curr = (left + right) // 2
            count = 0
            for i in piles:
                count += math.ceil(i/curr)
            if count <= h and ans > curr:
                ans = curr
                right = curr - 1
            else:
                left = curr + 1
        return ans
