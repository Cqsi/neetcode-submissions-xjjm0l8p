# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        stack = [cur]

        # generate the stack of the list
        while cur.next:
            cur = cur.next
            stack.append(cur)
        
        cur = head
        # while the cur and cur.next node is not the last element in the stack
        while cur != stack[-1] and cur.next != stack[-1]:
            tail = stack.pop() # get the tail
            tail.next = cur.next # assign the current cur.next node as the tail.next
            cur.next = tail # assign the cur.next as the tail
            cur = tail.next # cur goes two steps forward

        stack[-1].next = None # terminate the list