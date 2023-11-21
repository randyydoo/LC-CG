# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l_max, r_min = 2**31, -2**31-1 
        def dfs(root, l_max, r_min):
            if not root:
                return True

            elif root.val >= l_max or root.val <= r_min:
                return False

            return dfs(root.left, root.val, r_min) and dfs(root.right, l_max, root.val)

        return dfs(root,l_max,r_min)
