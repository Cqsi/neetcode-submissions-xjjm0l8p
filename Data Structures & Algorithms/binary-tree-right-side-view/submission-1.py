# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # Basically just BFS (level-by-level) and take the right-most element
        # of each row

        def bfs(root):
            if not root:
                return []
            
            result = []
            queue = deque([root])

            while queue:
                level_size = len(queue)

                i = 0
                while i < level_size:
                    node = queue.popleft()

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                    if i == level_size-1:
                        result.append(node.val)

                    i+=1
            
            return result
        
        return bfs(root)

                    
