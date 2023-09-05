# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        curr, fast = head, head.next

        while fast:
            if curr.val != fast.val:
                curr.next = fast
                curr = curr.next

            fast = fast.next

        if curr.next:
            curr.next = None

        return head
