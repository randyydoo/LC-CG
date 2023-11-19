class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) is 1: 
            return int(tokens[0])
        stack = []
        operators = {'+', '-' , '/', '*'}
        ans = 0
        for i in tokens:
            if i not in operators:
                stack.append(i)
                continue
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            if i is '+':
                stack.append(num1 + num2)
            elif i is '-':
                stack.append(num2 - num1)
            elif i is '*':
                stack.append(num1 * num2)
            elif i is '/':
                stack.append(math.trunc(num2/num1))
        return stack[0]

