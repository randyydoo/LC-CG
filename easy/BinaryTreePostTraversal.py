# Iterative Soluition
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)

            if node and node.left:
                stack.append(node.left)
            if node and node.right:
                stack.append(node.right)
        
        return ans[::-1]


# Recrusive Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)

        dfs(root)
        return ans
