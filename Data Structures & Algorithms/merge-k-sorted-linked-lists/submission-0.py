# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = list1
        cur2 = list2
        dummy = ListNode(0)
        res = dummy

        while cur1 and cur2:

            if cur1.val <= cur2.val:
                res.next = cur1
                cur1 = cur1.next
            else:
                res.next = cur2
                cur2 = cur2.next
            
            res = res.next
        
        res.next = cur1 if cur1 else cur2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        l = len(lists)

        if l == 0:
            return None
        if l == 1:
            return lists[0]

        res = []

        for i in range((l + 1) // 2):
            j = l - i - 1

            if i == j:
                res.append(lists[i])
            else:
                res.append(self.mergeTwoLists(lists[i], lists[j]))

        return self.mergeKLists(res)
    