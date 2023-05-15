class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {'}', ')', ']'}
        for i in s:
            stack.append(i)
            if i in close:
                if i is ']' and stack[stack.index(i) - 1] is '[':
                    stack.pop()
                    stack.pop()
                elif i is '}' and stack[stack.index(i) - 1] is '{':
                    stack.pop()
                    stack.pop()
                elif i is ')' and stack[stack.index(i) - 1] is '(':
                    stack.pop()
                    stack.pop()
        return len(stack) is 0
