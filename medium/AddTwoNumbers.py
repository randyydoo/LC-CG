# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        carry = 0
        p1, p2 = l1, l2

        while p1 or p2:
            total = carry
            if p1:
                total += p1.val
                p1 = p1.next
            if p2:
                total += p2.val
                p2 = p2.next
                
            carry = total // 10
            if total > 9:
                total = total % 10
            
            
            curr.next = ListNode(total)
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)
        return head.next
