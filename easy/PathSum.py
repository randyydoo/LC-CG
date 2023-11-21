# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(root, total):
            if not root:
                return

            total -= root.val 
            if not root.left and not root.right and total == 0:
                return True
            

            return dfs(root.left, total) or dfs(root.right, total) 
        
        return dfs(root, targetSum)
