class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        self.perimeter = 0
        visited = set()

        def dfs(row,col):

            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            visited.add((row, col))

            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                    self.perimeter += 1
                elif grid[r][c] == 1 and (r,c) not in visited:
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    dfs(r,c)
        
        return self.perimeter