class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.minheap = nums[:k]
        heapq.heapify(self.minheap)

        for i in range(k, len(nums)):
            if nums[i] > self.minheap[0]:
                heapq.heappushpop(self.minheap, nums[i])

    def add(self, val: int) -> int:
        if len(self.minheap) < self.kth:
            heapq.heappush(self.minheap, val)
        elif val > self.minheap[0]:
            heapq.heappushpop(self.minheap,val)
        return self.minheap[0]


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
