# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(s,root):
            nonlocal res
            if not root:
                return
            elif root:
                s += str(root.val)
            if root and not root.left and not root.right:
                res += int(s)
                return

            return dfs(s, root.left) or dfs(s, root.right)

        dfs('', root)
        return res
