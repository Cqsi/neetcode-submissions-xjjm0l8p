class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        # left = LRU, right = most recently used
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    # remove node from list
    def remove(self, node):
        # get previous and next node
        prev = node.prev
        nxt = node.next

        # update the nodes so that the middle node is no more
        prev.next = nxt
        nxt.prev = prev

    # insert node at right
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        # insert node in the middle
        prev.next = node
        nxt.prev = node

        # assign node prev and next
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            # we need to update the most recent node
            # we do this using the helper functions and first removing the Node
            # and then resinserting the node
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            # self.cache[key] gets us a node, so .val gets us the value
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if the key is already in the cache, we first remove it
        if key in self.cache:
            self.remove(self.cache[key])
        
        # make a new node and insert it
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # check capacity
        if len(self.cache) > self.cap:
            # we need to remove from the list and delete the LRU from the hashmap
            lru = self.left.next # this will always be the LRU
            self.remove(lru)
            del self.cache[lru.key]
