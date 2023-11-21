class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if stack and p == ']' and stack[-1] == '[':
                stack.pop()
            elif stack and p == '}' and stack[-1] == '{':
                stack.pop()
            elif stack and p == ')' and stack[-1] == '(':
                stack.pop()
            else:      
                stack.append(p)
    
        return len(stack) == 0
