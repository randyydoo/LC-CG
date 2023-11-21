class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, stack, total):
            nonlocal res
            if total == target:
                res.append(stack.copy())
                return
            if total >= target or i >= len(candidates):
                return 

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue 
                stack.append(candidates[j])
                dfs(j + 1, stack, total + candidates[j])
                stack.pop()

        dfs(0, [], 0)
        return res 
