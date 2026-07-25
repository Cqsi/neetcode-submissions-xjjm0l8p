import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        rows = len(heights)
        cols = len(heights[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        effort = [
            [float('inf')] * cols
            for _ in range(rows)
        ]
        effort[0][0] = 0
        min_heap = [(0,0,0)]

        while min_heap:

            current_effort, r, c = heapq.heappop(min_heap)

            if r == rows-1 and c == cols-1:
                return current_effort

            if current_effort > effort[r][c]:
                continue
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr <= rows-1 and 0 <= nc <= cols-1:
                    diff = abs(heights[r][c]-heights[nr][nc])
                    new_effort = max(current_effort, diff)

                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, nr, nc))

        return 0
