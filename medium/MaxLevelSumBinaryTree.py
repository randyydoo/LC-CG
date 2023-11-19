# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans, level, max_sum = 1, 1, root.val
        q = deque([root])

        while q:
            temp_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    temp_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if temp_sum > max_sum:
                max_sum = temp_sum
                ans = level

            level += 1
        return ans
