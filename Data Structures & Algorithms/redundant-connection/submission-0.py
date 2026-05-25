class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        N = len(edges)
        par = [i for i in range(N+1)] # i-th node -> parent
        rank = [1] * (N + 1)

        # return the representative node
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        # 
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return True

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return False
        
        for a, b in edges:
            if union(a, b):
                return [a, b]