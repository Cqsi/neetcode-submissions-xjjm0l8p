class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        best = [[float("inf")] * len(grid) for _ in range(len(grid))]
        best[0][0] = grid[0][0]
        heap = []
        heap.append((grid[0][0], 0, 0))

        while heap:
            cell, x, y = heapq.heappop(heap)
            

            if x == len(grid)-1 and y == len(grid)-1:
                return cell

            directions = [[0,1], [0, -1], [1,0], [-1, 0]]
            for direc in directions:
                dx, dy = direc
                if x+dx in range(len(grid)) and y+dy in range(len(grid)):
                    newTime = max(cell, grid[x+dx][y+dy])
                    if newTime < best[x+dx][y+dy]:
                        best[x+dx][y+dy] = newTime
                        heapq.heappush(heap, (newTime, x+dx, y+dy))