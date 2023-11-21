# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)

            return 1 + max(left,right)

        def insert(root,i, j, height, res):
            if not root:
                return
            print(i,j)
            res[i][j] = str(root.val)

            insert(root.left, i+1, j - (2**(height-i-1)), height, res)
            insert(root.right, i+1, j + (2**(height-i-1)), height, res)

            return res

        res = []
        height = height(root) - 1
        for i in range(height+1):
            temp = []
            for j in range(2**(height+1)-1):
                temp.append('')
            res.append(temp)

        middle = len(res[0])//2
        return insert(root,0,middle,height,res)
