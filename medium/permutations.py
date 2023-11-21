class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)

        def perms(used, stack):
            if len(stack) == len(nums):
                ans.append(stack.copy())
                return
            
            for i in range(len(nums)):
                print(i, used)
                if not used[i]:
                    used[i] = True
                    stack.append(nums[i])
                    perms(used, stack)
                    stack.pop()
                    used[i] = False        

        perms(used, [])
        return ans
