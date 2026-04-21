# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = 0
        cur = l1
        c = 0
        while cur:
            s += cur.val*10**c
            c += 1
            cur = cur.next

        cur = l2
        c = 0
        while cur:
            s += cur.val*10**c
            c += 1
            cur = cur.next

        print(s)

        res = ListNode(0)
        c = res
        number = str(s)[::-1]
        l = len(number)
        i = 0
        while i < l:
            c.next = ListNode(int(number[i]))
            c = c.next
            i += 1

        return res.next

