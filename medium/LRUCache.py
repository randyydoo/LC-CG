class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = capacity
        self.q = collections.deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.q.remove(key)
            self.q.append(key)
            return self.cache[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.size and key not in self.cache:
            rem = self.q.popleft()
            del self.cache[rem]
        if key in self.q:
            self.q.remove(key)
        self.cache[key] = value
        self.q.append(key)
