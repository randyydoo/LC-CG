class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if not stack or stack[-1][0] >= temperatures[i]:
                stack.append((temperatures[i], i))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    val, j = stack.pop()
                    res[j] = i-j
                stack.append((temperatures[i], i)) 
        return res
