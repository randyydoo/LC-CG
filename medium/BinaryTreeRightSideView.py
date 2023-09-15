# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def update(q, length):
            for i in range(length):
                node = q.popleft()
                
                q.append(node.left) if node and node.left else None
                q.append(node.right) if node and node.right else None

            return q

        right_q = deque([root.right]) if root.right else deque([])
        left_q = deque([root.left]) if root.left else deque([])
        ans = [root.val]

        while right_q or left_q:
            if len(right_q) > 0:
                node = right_q[-1]
            else:
                node = left_q[-1]
            ans.append(node.val) if node else None

            right_q = update(right_q, len(right_q))        
            left_q = update(left_q, len(left_q))

        return ans
