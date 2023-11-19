class RandomizedSet:

    def __init__(self):
        self.indexes = {} # val:index
        self.stack = [] 
        

    def insert(self, val: int) -> bool:
        if val not in self.indexes:
            length = len(self.stack)
            self.indexes[val] = length
            self.stack.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.indexes:
            i = self.indexes[val]
            swap = self.stack[-1]

            self.indexes[swap] = i
            self.stack[i], self.stack[-1] = swap, val
            self.stack.pop()

            del self.indexes[val]
            return True

        return False

    def getRandom(self) -> int:
        return self.stack[randint(0,len(self.stack)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
