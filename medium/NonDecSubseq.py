class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        
        def dfs(i, prev, stack):
            if i==len(nums):
                if len(stack)>=2:
                    res.add(tuple(stack.copy()))
                return
                
            dfs(i+1, prev, stack)

            if nums[i]>=prev:
                stack.append(nums[i])
                dfs(i+1, nums[i], stack)
                stack.pop()
        
        dfs(0, -inf, [])
        return list(res)
