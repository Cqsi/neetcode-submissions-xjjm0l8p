# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # move right pointer n steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1

        
        # move left and right pointer until right hits the end
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next