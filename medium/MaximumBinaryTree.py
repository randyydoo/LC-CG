# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode(max(nums))
        index = nums.index(max(nums))
        left, right = nums[:index], nums[index+1:]

        def dfs(root, left, right):
            if left:
                left_max = max(left)
                index = left.index(left_max)
                root.left = TreeNode(left_max)
                dfs(root.left, left[:index], left[index+1:])

            if right:
                right_max = max(right)
                index = right.index(right_max)
                root.right = TreeNode(right_max)
                dfs(root.right, right[:index], right[index+1:])
            
            return root

        return dfs(root, left, right)
