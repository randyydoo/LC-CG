class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)

        for i in range(len(cost)-1, -1, -1):
            if i != len(cost)-1:
                dp[i] = min(cost[i]+ dp[i+1], cost[i] + dp[i+2])
            else:
                dp[i] = cost[i]
        
        return min(dp[0],dp[1])
