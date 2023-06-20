# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        middle, end = head, head.next
        while end and end.next:
            middle = middle.next
            end = end.next.next

        newHead, prev, middle.next= middle.next, None, None
        while newHead:
            nxt = newHead.next
            newHead.next = prev
            prev = newHead
            newHead = nxt
        left,right = head, prev
        
        while left and right:
           left_next, right_next = left.next, right.next
           right.next = left_next
           left.next = right
           left, right = left_next, right_next

