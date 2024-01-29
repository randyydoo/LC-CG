# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p1_prev = p1 = head
        for _ in range(left-1):
            p1_prev = p1
            p1 = p1.next

        p2 = head 
        for _ in range(right):
            p2 = p2.next
        
        p3_prev, p3 = None, p1
        for _ in range(right-left+1):
            temp = p3.next
            p3.next = p3_prev
            p3_prev = p3
            p3 = temp

        p1_prev.next = p3_prev
        p1.next = p3

        return head if head != p1 else p3_prev
