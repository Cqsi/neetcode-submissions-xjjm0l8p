# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Strategy
        # 1. we want to do DFS
        # 2. We want to start counter from the smallest element, i.e. the one to the most left
        # 3.

        self.count = 0
        self.result = 0  # ← store the answer here

        def dfs(node):
            if not node:
                return

            dfs(node.left)

            self.count += 1
            if self.count == k:
                self.result = node.val  # ← save the value when count hits k
                return

            dfs(node.right)

        dfs(root)
        return self.result  