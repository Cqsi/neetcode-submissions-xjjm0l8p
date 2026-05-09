# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # strategy
        # 1. dfs through every node and get the max left height and right height
        # 2. take the difference of them
        # 3. if larger than 1, return False

        self.balanced = True

        def height(node):

            if not node:
                return 0
            
            lh = height(node.left)
            rh = height(node.right)

            if abs(lh - rh) > 1:
                self.balanced = False
            
            return 1 + max(lh, rh)

        height(root)
        return self.balanced