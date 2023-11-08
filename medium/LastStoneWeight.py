class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)

            if x == y:
                continue
            else:
                diff = max(abs(x), abs(y)) - min(abs(x), abs(y))
                heapq.heappush(stones, diff*-1)
        
        return abs(stones[0]) if stones else 0
