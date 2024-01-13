# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        res, adj = 0, defaultdict(list)
        def build(root):
            nonlocal adj
            if not root:
                return
            if root.left:
                adj[root.val].append(root.left.val)
                adj[root.left.val].append(root.val)
            if root.right:
                adj[root.val].append(root.right.val)
                adj[root.right.val].append(root.val)
            build(root.left)
            build(root.right)
            return
        def dfs(curr, ct, visited):
            nonlocal res
            res = max(ct, res)
            visited.add(curr)
            for neigh in adj[curr]:
                if neigh not in visited:
                    dfs(neigh, ct+1, visited)
            return 

        build(root)
        dfs(start, 0, set())

        return res
