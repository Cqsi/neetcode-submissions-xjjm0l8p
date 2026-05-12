# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # strategy 
        # 1. 

        self.max_sum = float("-inf")

        def dfs(node):
            if not node:
                return 0
            
            vl = max(dfs(node.left), 0)
            vr = max(dfs(node.right), 0)

            self.max_sum = max(self.max_sum, node.val+vl+vr)

            if vl >= vr:
                return node.val + vl
            else:
                return node.val + vr
            

        dfs(root)
        return self.max_sum