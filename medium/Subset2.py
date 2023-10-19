class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        def helper(i, stack):
            if i >= len(nums):
                ans.add(tuple(stack.copy()))
                return
                
            stack.append(nums[i])
            helper(i+1, stack)
            stack.pop()
            helper(i+1,stack)

        helper(0,[])
        return list(ans)
