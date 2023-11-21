class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        res, heap = 0, []

        for i in range(len(dist)):
            heapq.heappush(heap, dist[i]/speed[i])

        while heap:
            if heapq.heappop(heap) <= res:
                break
            res += 1

        return res
