# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        ans = []
        c = 0

        while q:
            temp_ans = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    temp_ans.append(node.val)
                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)

            if temp_ans and c % 2 == 0:  
                ans.append(temp_ans) 
            elif temp_ans:
                ans.append(temp_ans[::-1])
            c+=1

        return ans
