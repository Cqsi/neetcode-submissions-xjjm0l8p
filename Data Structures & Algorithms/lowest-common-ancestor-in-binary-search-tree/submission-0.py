# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # self.res = 0

        # def dfs(node):

            # def c(n):
                # return n.val == p.val or n.val = q.val 

            # if not node:
                # return False
            
            # 1. we need to return true when the cur val equals either p or q
            # since the values are unique, it's enough
            
            # 2. which cases are there?
            # - both dfs are true -> return true
            # - 

            # if (c(node) and dfs(node.left)) or (c(node) and dfs(node.right)) or (dfs(node.left) and dfs(node.right)):

            # Solution was much easier than I thought since it's a BST

            def h(node):

                if not node:
                    return None
                elif p.val < node.val and q.val < node.val:
                    return h(node.left)
                elif p.val > node.val and q.val > node.val:
                    return h(node.right)
                else:
                    return node
                
            return h(root)
