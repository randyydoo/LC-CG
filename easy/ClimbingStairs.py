class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n-2)
        dp.append(1) 
        dp.append(1)
     
        for i in range(n-3,-1,-1):
            dp[i] = dp[i+1] + dp[i+2]
     
        return dp[0] + dp[1] if n > 1 else 1
