# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = []
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        size = length//k
        curr = head
        extra = length % k
        for i in range(k):
            temp = curr
            for j in range(size-1):
                if curr:
                    curr = curr.next
            if extra > 0 and i < extra and curr and length > k:
                    curr = curr.next
            temp_next = curr.next if curr else None
            if curr:
                curr.next = None
            ans.append(temp)
            curr = temp_next 
        return ans
