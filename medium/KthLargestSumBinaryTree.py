Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        lst = list()

        while q:
            temp_sum = 0
            for i in range(len(q)):
                node = q.popleft()

                if node:
                    temp_sum += node.val
                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)

            lst.append(temp_sum)

        lst = sorted(lst, reverse=True)
        return lst[k-1] if k <= len(lst) else -1

