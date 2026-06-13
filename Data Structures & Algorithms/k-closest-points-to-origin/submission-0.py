class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(point: List[int]) -> int:
            x, y = point
            return x*x + y*y
        
        return heapq.nsmallest(k, points, key=distance)