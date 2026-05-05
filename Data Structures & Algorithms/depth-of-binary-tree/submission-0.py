# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        md = 0

        def depth(node, d):

            if not node:
                return d

            d += 1
            return max(depth(node.left, d), depth(node.right, d))

        return depth(root, 0)