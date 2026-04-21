"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        h = {}
        copy = Node(0)
        cur = head

        while cur:
            copy.next = Node(cur.val, cur.next, cur.random)
            h[cur] = copy.next
            cur = cur.next
            copy = copy.next

        cur = head
        while cur:
            if not cur.next :
                h[cur].next = None
            else:
                h[cur].next = h[cur.next]

            if not cur.random:
                h[cur].random = None
            else:
                h[cur].random = h[cur.random]
            cur = cur.next
        
        return h[head]

        