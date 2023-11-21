# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        bank1, bank2 = [], []
        def dfs(node, num: int):
            nonlocal bank1
            nonlocal bank2

            if not node:
                bank1.append(None) if num == 1 else bank2.append(None)
                return 0

            bank1.append(node.val) if num == 1 else bank2.append(node.val)

            dfs(node.left,num)
            dfs(node.right,num)

            return 0

        dfs(p,1)
        dfs(q,2)
        return bank1 == bank2
