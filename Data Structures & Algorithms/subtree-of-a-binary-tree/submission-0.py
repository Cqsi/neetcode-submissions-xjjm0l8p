# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(p, q):
            self.same = True

            def dfs(n1, n2):

                if not n1 and not n2:
                    return
                
                if not n1 or not n2 or n1.val != n2.val:
                    self.same = False
                else:
                    dfs(n1.left, n2.left)
                    dfs(n1.right, n2.right)
            
            dfs(p, q)
            return self.same

        self.res = False

        def sim(node):

            if not node:
                return
            
            if node.val == subRoot.val:
                if sameTree(node, subRoot):
                    self.res = True
            
            sim(node.left)
            sim(node.right)
        
        sim(root)
        return self.res
