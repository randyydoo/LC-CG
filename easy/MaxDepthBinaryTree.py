# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans, stack =  1, [[root,1]]

        while stack:
            node, height = stack.pop()
            ans = max(ans,height)
            stack.append([node.left, height+1]) if node.left else None
            stack.append([node.right, height+1]) if node.right else None
        
        return ans
