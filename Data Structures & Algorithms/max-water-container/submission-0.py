class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo = 0
        hi = len(heights)-1
        m = 0
        while lo<hi:
            m = max(m, min(heights[lo], heights[hi])*(hi-lo))
            if heights[lo]>=heights[hi]:
                hi -= 1
            else:
                lo += 1

        return m