# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False

        seen = set()
        cur = head
        seen.add(cur)

        while cur.next:
            
            if cur.next not in seen:
                cur = cur.next
                seen.add(cur)
            else:
                return True

        return False