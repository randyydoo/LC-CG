# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0

        def dfs(root):
            if not root:
                return

            get_sum(root, 0)
            return dfs(root.left) or dfs(root.right)

        def get_sum(root, curr_sum):
            nonlocal res
            if not root:
                return
            if curr_sum + root.val == targetSum:
                res += 1

            get_sum(root.left, curr_sum + root.val) 
            get_sum(root.right, curr_sum + root.val)

        dfs(root)
        return res
