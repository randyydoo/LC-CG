    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        i = 0
        while i <= len(temperatures) - 1:
            top = len(stack) - 1
            temp = temperatures[i]
            if len(stack) == 0 or temp <= stack[top][1]:
                stack.append([i, temp])
                i += 1
            elif temp > stack[top][1]:
                ans[stack[top][0]] = i - stack[top][0]
                stack.pop()
        return ans
