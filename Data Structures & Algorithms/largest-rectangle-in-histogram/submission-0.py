class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        l = len(heights)
        wr = [0] * l
        wl = [0] * l
        stack = []

        # left to right
        for i, h in enumerate(heights):
            while stack and h<stack[-1][1]:
                ci, ch = stack.pop()
                wr[ci] = i-ci-1
            stack.append((i, h))

        while stack:
            ci, ch = stack.pop()
            wr[ci] = l-ci-1

        # right to left
        for i, h in enumerate(reversed(heights)):
            while stack and h<stack[-1][1]:
                ci, ch = stack.pop()
                wl[ci] = i-ci-1
            stack.append((i, h))

        while stack:
            ci, ch = stack.pop()
            wl[ci] = l-ci-1
        
        wl.reverse()
        # calculate max rectangle
        max_rec = 0
        for i in range(l):
            rec = (wr[i]+wl[i]+1)*heights[i]
            max_rec = max(max_rec, rec)

        return max_rec