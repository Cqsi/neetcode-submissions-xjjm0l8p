# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        d = ListNode(0)
        c = d
        l1 = list1
        l2 = list2
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    c.next = l1
                    l1 = l1.next
                else:
                    c.next = l2
                    l2 = l2.next
            elif l1:
                c.next = l1
                l1 = l1.next
            elif l2:
                c.next = l2
                l2 = l2.next
            c = c.next
        
        return d.next