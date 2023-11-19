class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        stack = []

        def dfs(i):
            if sum(stack) == target:
                ans.append(stack.copy())
                return
            
            if sum(stack) > target or i >= len(candidates):
                return

            stack.append(candidates[i])
            dfs(i)
            stack.pop()
            dfs(i+1)

        dfs(0)
        return ans
