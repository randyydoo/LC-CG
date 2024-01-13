# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return [float('inf'), float('-inf')]

            left = dfs(root.left)
            right = dfs(root.right)

            min_val = min(root.val, left[0], right[0])
            max_val = max(root.val, left[1], right[1])

            res = max(res, abs(root.val-min_val), abs(root.val-max_val))
            return [min_val, max_val]


        dfs(root) 
        return res
