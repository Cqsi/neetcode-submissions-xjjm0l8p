# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxv):

            if not node:
                return 0
            
            if node.val >= maxv:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            else:
                return dfs(node.left, maxv) + dfs(node.right, maxv)
        
        return dfs(root, -200)

            