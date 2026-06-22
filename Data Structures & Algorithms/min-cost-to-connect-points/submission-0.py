class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        visited = set()
        heap = [(0, 0)] # distance, point index
        totalCost = 0

        while len(visited) != n:
            cost, i = heapq.heappop(heap)

            if i in visited:
                continue

            visited.add(i)
            totalCost += cost
            x1, y1 = points[i]

            for j in range(n):
                if j not in visited:
                    x2, y2 = points[j]
                    distance = abs(x2-x1)+abs(y2-y1)
                    heapq.heappush(heap, (distance, j))

        return totalCost