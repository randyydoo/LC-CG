class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {')' : '(', '}' : '{', ']' : '['}
        for i in s:
            stack.append(i)
            if i in close:
                if close[i] == stack[0] and stack[stack.index(i) - 1] in close:
                    del stack[0]
                    stack.pop()
                elif close[i] == stack[stack.index(i) - 1]:
                    stack.pop()
                    stack.pop()
        return len(stack) is 
