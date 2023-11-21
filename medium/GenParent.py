class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(op, close, s):
            if len(s) == n * 2:
                ans.append(s)
                return
            if op < n:
                backtrack(op+1, close, s + "(")
            if op > close:
                backtrack(op,close+1,s + ")")
        
        backtrack(0,0,'')
        return ans
             
