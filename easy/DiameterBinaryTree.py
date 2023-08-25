# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # case1: diameter = left + right + 1
        # case2: diamater = max(left,right) if max(left,right) > left + right + 1
        ans = 0

        def getLength(node):
            nonlocal ans

            if not node:
                return 0

            left = getLength(node.left)
            right = getLength(node.right)
            ans = max(ans, left+right)

            return 1 + max(left,right) 

        getLength(root)
        return ans
