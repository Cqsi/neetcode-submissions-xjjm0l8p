class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1:
            return False

        g = {i: [] for i in range(n)}

        for n1, n2 in edges:
            g[n1].append(n2)
            g[n2].append(n1)

        seen = set()

        def dfs(node):

            if node in seen:
                return 

            seen.add(node)

            for nei in g[node]:
                dfs(nei)

        dfs(0)      
        return len(seen) == n
        