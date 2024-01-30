# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serial = ''
        def dfs(root):
            nonlocal serial
            if not root:
                serial += 'null,'
                return 0
            serial += str(root.val) + ','
            left = dfs(root.left)
            right = dfs(root.right)
            return 
        dfs(root)
        return serial 



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        i = 0
        data = data.split(',')
        def dfs():
            nonlocal i
            if data[i] == 'null' or i >= len(data):
                return None

            root = TreeNode(int(data[i]))
            i += 1
            root.left = dfs()
            i += 1
            root.right = dfs()
            return root

        return dfs() 


# deser = Codec()
# ans = deser.deserialize(ser.serialize(root)
