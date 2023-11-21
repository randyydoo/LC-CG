class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i, stack):
            if i >= len(s):
                res.append(stack.copy())
                return

            for j in range(i, len(s)):
                c_str = s[i:j+1]
                if c_str == c_str[::-1]:
                    stack.append(c_str)
                    dfs(j+1, stack)
                    stack.pop()

            return 

        dfs(0, []) 
        return res
