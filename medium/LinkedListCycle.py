# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        passed = set()
        curr = head
        while curr:
            if curr in passed:
                return True
            passed.add(curr)
            curr = curr.next
        return False
