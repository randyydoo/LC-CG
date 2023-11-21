# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curr_max = root.val
        ans = 0

        def dfs(node, curr_max):
            nonlocal ans

            if not node:
                return 0

            if node.val >= curr_max:
                ans += 1
            curr_max = max(node.val, curr_max)

            return dfs(node.left, curr_max) or dfs(node.right, curr_max)
        
        dfs(root, curr_max)
        return ans
