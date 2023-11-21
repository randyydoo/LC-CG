class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, (0,0))]
        m, n = len(heights), len(heights[0])
        memo = [[float('inf')] * n for _ in range(m)]
        memo[0][0] = 0

        while heap:
            cost, index = heapq.heappop(heap)
            i,j = index[0], index[1]

            if i == m-1 and j == n-1:
                return cost

            dirs = [[0,1], [1,0], [0,-1], [-1,0]]
            for x, y in dirs:
                if 0 <= i+x < m and 0 <= j+y < n:
                    prev_cost, nxt_cost = heights[i][j] , heights[i+x][j+y]
                    new_cost =  max(cost,abs(prev_cost-nxt_cost))
                    if new_cost < memo[i+x][j+y]:
                        memo[i+x][j+y] = new_cost
                        heapq.heappush(heap, (new_cost, (i+x,j+y)))

        return 0
