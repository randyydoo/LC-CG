class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        stack = []

        def dfs(i):
            if i > len(nums) - 1:
                ans.append(stack.copy())
                return
            stack.append(nums[i])
            dfs(i+1)

            stack.pop()
            dfs(i+1)

            return

        dfs(0)
        return ans
