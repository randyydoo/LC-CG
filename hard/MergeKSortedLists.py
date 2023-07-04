# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return ListNode().next
        store = []
        store.append(lists[0])

        def helper(lst1, lst2):
            dummy = ListNode()
            curr = dummy
            while lst1 and lst2:
                if lst1.val <= lst2.val:
                    curr.next = lst1
                    lst1 = lst1.next
                else:
                    curr.next = lst2
                    lst2 = lst2.next
                curr = curr.next
            if lst1:
                curr.next = lst1
            elif lst2:
                curr.next = lst2
            return dummy.next

        for i in range(1,len(lists)):
            store[0] = helper(store[0], lists[i])
            
        return store[0]
