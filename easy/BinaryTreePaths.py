# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(root, s):
            nonlocal ans
            if not root:
                return 
                
            elif not root.left and not root.right:
                s += f"{root.val}"
                ans.append(s)

            s += f"{root.val}->"
            dfs(root.left,s)
            dfs(root.right,s)
                
            return

        dfs(root, '')
        return ans
