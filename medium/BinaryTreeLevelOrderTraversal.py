# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque([root])

        while q:
            length = len(q)
            temp = []
            for i in range(length):
                node = q.popleft()
                temp.append(node.val) if node else None
                q.append(node.left) if node and node.left else None
                q.append(node.right) if node and node.right else None

            ans.append(temp) if len(temp) > 0 else None
            
        return ans
