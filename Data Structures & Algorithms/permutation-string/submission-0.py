class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        chars = {}
        l = 0
        r = 0

        if len(s1) > len(s2):
            return False

        for c in s1:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1

        counter = {}
        while r < len(s2):

            c = s2[r]
            if c not in chars:
                r += 1
                l = r
                counter = {}
            else:
                if c in counter:
                    counter[c] += 1
                else:
                    counter[c] = 1

                while counter[c] > chars[c]:
                    cl = s2[l]
                    counter[cl] -= 1
                    if counter[cl] == 0:
                        del counter[cl]
                    l += 1
                
                if counter == chars:
                    return True
            
                r += 1
        
        return False
