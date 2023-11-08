class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for x, y in points:
            dist = math.sqrt(x**2+y**2)
            heapq.heappush(heap, (dist, x, y))

        while len(res) < k:
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])

        return res
