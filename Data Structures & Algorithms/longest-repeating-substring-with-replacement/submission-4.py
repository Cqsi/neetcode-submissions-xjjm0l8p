class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # idea
        # 1. keep track of number of each character using a hash table
        # 2. do a sliding window

        h = {} # char -> number (amount)
        l = 0
        r = 0
        res = 0
        max_character = ""
        max_character_amount = 0
        ee = 0

        while r < len(s):

            c = s[r]
            if c not in h:
                h[c] = 1
            else:
                h[c] += 1
            
            if h[c] > max_character_amount:
                max_character_amount = h[c]
            
            ee = (r-l+1) - max_character_amount

            # i.e. we have more characters than k of the type that is not the max char
            while ee > k and l < r:
                cl = s[l]
                h[cl] -= 1
                max_character_amount = max(h.values())
                ee = (r-l) - max_character_amount
                l += 1
                
            print(h)
            res = max(res, r-l+1)
            r += 1
        
        return res