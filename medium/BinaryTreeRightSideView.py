# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(q, length):
            for i in range(length):
                node = q.popleft()
                
                q.append(node.left) if node and node.left else None
                q.append(node.right) if node and node.right else None

            return q
 # hell
        q = deque([root]) if root else deque([])
        ans = []

        while q:
            node = q[-1]
            ans.append(node.val) if node else None

            q = bfs(q, len(q))        

        return ans
