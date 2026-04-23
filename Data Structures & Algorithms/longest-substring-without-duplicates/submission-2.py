class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        max_length = 0
        lo = 0
        hi = 0
        while hi < len(s):
            if s[hi] in h and h[s[hi]] >= lo:
                lo = h[s[hi]] + 1
            h[s[hi]] = hi
            max_length = max(max_length, hi - lo + 1)
            hi += 1
        return max_length


                