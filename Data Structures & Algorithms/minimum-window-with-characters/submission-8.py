class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Strategy:
        # 1. First we make a dict of the chars in t
        # 2. Then we init variables for the main procedure. Example: the need_satisfied is
        # keeping track of how many chars we "need satisfied" i.e. more than or equal amounts.
        # We do this to not have to compare the dictionairies between each other
        # 3. We use sliding windows technique using a left and right pointer
        # 4. We increase the right pointer until we have a dictionary that cotains enough chars
        # so that t_chars is "contained" within it
        # 5. The we minimize the current substring by increase the left pointer as much as possible
        # Here two possibilities exist: (1) that the current char s[l] is not in t_chars, then we
        # just continue l+1 or (2) it is in t_char, then we have to check whether we can increase l
        # and still maintain equality between have_satisfied and need_satisfied

        # Make dict for chars in t
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