class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        self.max_area = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            area = 0

            while q:
                row, col = q.popleft() # important to use .popleft and not .pop
                area += 1
                
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))
            
            self.max_area = max(self.max_area, area)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs(r, c)
        
        return self.max_area

