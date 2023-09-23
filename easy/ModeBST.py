# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = {}
        ans = []
        def dfs(root):
            nonlocal d

            if not root:
                return
            elif root.val in d:
                d[root.val] += 1
            else:
                d[root.val] = 1

            return dfs(root.left) or dfs(root.right)
        dfs(root) 
        count = max(d.values())
        for k,v in d.items():
            if v == count:
                ans.append(k)
                
        return ans
