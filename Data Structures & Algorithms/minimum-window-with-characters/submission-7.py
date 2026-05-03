class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_chars = {}

        for c in t:
            if c in t_chars:
                t_chars[c] += 1
            else:
                t_chars[c] = 1

        need_satisfied = len(t_chars)

        l = 0
        r = 0
        cur = {}
        res = ""
        min_res = float('inf')
        have_satisfied = 0

        while r < len(s):

            sc = s[r]

            if sc in cur:
                cur[sc] += 1
            else:
                cur[sc] = 1

            if sc in t_chars and cur[sc] == t_chars[sc]:
                have_satisfied += 1
            
            while have_satisfied == need_satisfied and l <= r:
                if r-l+1 <= min_res:
                    min_res = r-l+1
                    res = s[l:r+1] 
                cur[s[l]] -= 1
                if s[l] in t_chars and cur[s[l]] < t_chars[s[l]]:
                    have_satisfied -= 1
                l+=1 

            r += 1

        return res