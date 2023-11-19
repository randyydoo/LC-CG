"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        d = {None:None}
        while curr:
            d[curr] = Node(curr.val)
            curr = curr.next
        newCurr = head
        while newCurr:
            newNode = d[newCurr]
            newNode.next = d.get(newCurr.next)
            newNode.random = d.get(newCurr.random)
            newCurr = newCurr.next
        return d[head]
