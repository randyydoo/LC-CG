# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p1, p2 = ListNode(), ListNode()
        p1_dummy, p2_dummy = p1, p2
        while head:
            temp = head.next
            head.next = None
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = temp
        
        p1.next = p2_dummy.next
        return p1_dummy.next
