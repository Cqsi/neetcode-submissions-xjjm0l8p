class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}
        
        for s in strs:
            lc = "".join(sorted(s))
            if lc in seen:
                seen[lc].append(s)
            else:
                seen[lc] = [s]

        return list(seen.values())