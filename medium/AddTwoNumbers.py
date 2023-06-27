# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ans = dummy
        curr1, curr2 = l1, l2
        carry = 0
        while curr1 and curr2:
            s = curr1.val + curr2.val + carry
            if s > 9:
                carry = s // 10
                ans.next = ListNode(s % 10)
            else:
                carry = 0
                ans.next = ListNode(s)
            ans, curr1, curr2 = ans.next, curr1.next, curr2.next
        while curr1:
            s = curr1.val + carry
            if s > 9:
                carry = s // 10
                ans.next = ListNode(s % 10)
            else:
                carry = 0
                ans.next = ListNode(s)
            ans, curr1 = ans.next, curr1.next
        while curr2:
            s = curr2.val + carry
            if s > 9:
                carry = s // 10
                ans.next = ListNode(s % 10)
            else:
                carry = 0
                ans.next = ListNode(s)
            ans, curr2 = ans.next, curr2.next
        if carry == 1:
            ans.next = ListNode(1)
        return dummy.next
