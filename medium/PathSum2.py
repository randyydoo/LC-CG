# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = [] 
        def dfs(root, bank):
            nonlocal ans

            if not root:
                return

            bank.append(root.val)
            if sum(bank) == targetSum and not root.left and not root.right:
                ans.append(bank.copy())

            dfs(root.left, bank)
            dfs(root.right, bank)
            bank.pop()
            
        dfs(root, [])
        return ans
