class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # I spent quite a lot of time on this exercise
        # However I think this is a classic example of a problem that is very logical
        # once you find the correct idea
        
        # Idea: We do BFS from the treasure chests

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q = collections.deque()

        def addLand(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in visit or grid[r][c] == -1:
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: # -> a treasure chest
                    q.append([r,c])
                    visit.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)): # -> go through all current elements in q
                r, c = q.popleft()
                grid[r][c] = dist # -> for the first run dist = 0, so treasure chests will continue to be 0
                addLand(r+1, c)
                addLand(r-1, c)
                addLand(r, c+1)
                addLand(r, c-1)
            dist +=1