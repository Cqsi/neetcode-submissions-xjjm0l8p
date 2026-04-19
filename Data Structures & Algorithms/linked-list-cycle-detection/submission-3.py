# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # O(n) memory using a HashTable (i.e. set)

        # if not head:
        #     return False

        # seen = set()
        # cur = head
        # seen.add(cur)

        # while cur.next:
            
        #     if cur.next not in seen:
        #         cur = cur.next
        #         seen.add(cur)
        #     else:
        #         return True

        # return False

        # O(1) memory using slow and fast pointer
        if not head or not head.next:
            return False
        
        slow = head
        fast = head

        while fast.next and fast.next.next:

            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        
        return False
        