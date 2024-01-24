# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root, cts):
            nonlocal res
            if not root:
                return res

            cts[root.val] += 1
            if not root.left and not root.right:
                temp = 0
                for val in cts.values():
                    if val%2 != 0:
                        temp += 1
                if temp <= 1:
                    res += 1
            dfs(root.left, cts)
            dfs(root.right, cts)
            cts[root.val] -= 1
            return res

        return dfs(root, defaultdict(int))
