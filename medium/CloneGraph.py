"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {} 
        def dfs(node):
            nonlocal nodes
            if node in nodes:
                return

            copy = Node(node.val) 
            nodes[node] = copy
            for neighbor in node.neighbors:
                dfs(neighbor) 
                copy.neighbors.append(nodes[neighbor])

            return copy

        return dfs(node) if node else None
