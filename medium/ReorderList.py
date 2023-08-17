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
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tempHead, prev, slow.next = slow.next, None, None
        while tempHead:
            temp = tempHead.next
            tempHead.next = prev
            prev = tempHead
            tempHead = temp
        
        l1, l2 = head, prev
        while l1 and l2:
            l1_temp, l2_temp = l1.next, l2.next
            l2.next = l1_temp
            l1.next = l2
            l1, l2 = l1_temp, l2_temp
