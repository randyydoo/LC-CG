# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        stack = []

        while head:
            temp = head.next
            head.next = None
            stack.append(head)
            if len(stack) == k:
                while stack:
                    curr.next = stack.pop()
                    curr = curr.next
            head = temp

        for node in stack:
            curr.next = node
            curr = curr.next

        return dummy.next
