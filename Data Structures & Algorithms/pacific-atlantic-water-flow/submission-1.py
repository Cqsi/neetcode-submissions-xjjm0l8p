class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # idea: DFS from oceans inwards

        rows = len(heights)
        cols = len(heights[0])
        pacific_visit = set()
        atlantic_visit = set()

        def dfs(r, c, prev, isPacific):

            if r not in range(rows) or c not in range(cols):
                return

            cur = heights[r][c]
            
            if prev > cur:
                return
            
            if isPacific:
                if (r,c) in pacific_visit:
                    return
                pacific_visit.add((r, c))
            else:
                if (r,c) in atlantic_visit:
                    return
                atlantic_visit.add((r, c))

            dfs(r+1, c, cur, isPacific)
            dfs(r-1, c, cur, isPacific)
            dfs(r, c+1, cur, isPacific)
            dfs(r, c-1, cur, isPacific)
            


        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    dfs(r, c, 0, True)
                if r == rows-1 or c == cols-1:
                    dfs(r, c, 0, False)

        res = list(pacific_visit & atlantic_visit)
        return res