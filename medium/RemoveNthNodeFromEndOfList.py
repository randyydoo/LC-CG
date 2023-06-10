# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        left, right = dummy, dummy
        for i in range(n):
            right = right.next
        while True:
            temp = left.next
            connect = temp.next
            if right.next is None:
                left.next = connect
                return dummy.next
            else:
                left = left.next
                right = right.next
