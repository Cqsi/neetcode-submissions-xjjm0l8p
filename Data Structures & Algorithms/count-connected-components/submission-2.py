class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        g = {i: [] for i in range(n)}

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        visit = set()

        def dfs(node):

            if node in visit:
                return
            
            visit.add(node)

            for n in g[node]:
                dfs(n)
        
        components = 0
        for i in range(n):
            if i not in visit:
                components += 1
                dfs(i)
        
        return components