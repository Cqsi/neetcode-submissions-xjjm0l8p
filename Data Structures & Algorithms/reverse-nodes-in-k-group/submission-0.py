# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        cur = head

        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Idea (quite straightforward)
        # - We use recursion, where we pass in the head of the next group
        # - We go left to right, processing the groups one-by-one
        # - First we check whether the the next group can be k nodes long, and if not we return it as it is

        group_next = head
        for _ in range(k):
            if group_next is None:
                return head
            group_next = group_next.next
        
        prev = None
        cur = head

        # normal reversing of linked list (using three variables)
        # One change: stop while loop when cur reached group_next
        while cur is not group_next:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n

        # Original head is now the tail, and we want to set  athe next of the tail
        head.next = self.reverseKGroup(group_next, k)
        
        # prev is this group's new first node
        return prev


