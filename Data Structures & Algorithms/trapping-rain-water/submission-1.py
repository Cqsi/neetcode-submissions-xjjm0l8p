class Solution:
    def trap(self, height: List[int]) -> int:
        
        h = height
        height = [0] + height + [0]
        prefix = []
        suffix = []
        l = len(height)

        m = 0
        for i in range(1, l-1):
            prefix.append(m)
            m = max(m, height[i])

        m = 0
        for i in range(l-2, 0, -1):
            suffix.insert(0, m)
            m = max(m, height[i])
        
        print(prefix)
        print(suffix)
        w = 0
        for i in range(l-2):
            w += max(min(prefix[i], suffix[i])-h[i], 0)
        
        return w