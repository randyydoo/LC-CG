class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        PositionSpeed = []
        stack = []
        for i in range(len(position)):
            PositionSpeed.append([position[i], speed[i]])
        for pos,speed in sorted(PositionSpeed)[::-1]:
            stack.append((target - pos) / speed)
            if len(stack) > 1 and (target - pos) / speed <= stack[-2]:
                stack.pop()
        return len(stack)
            
