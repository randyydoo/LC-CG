# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node, curr = dummy, head
        while curr and curr.next:
            temp, temp2 = curr.next, curr.next.next
            curr.next = None
            temp.next = curr
            node.next = temp
            node = node.next.next
            curr = temp2
        if curr:
            node.next = curr
        return dummy.next
