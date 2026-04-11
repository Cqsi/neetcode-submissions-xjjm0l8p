class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        seen = {}
        
        for s in strs:
            lc = "".join(sorted(s))
            if lc in seen:
                seen[lc].append(s)
            else:
                seen[lc] = [s]

        return list(seen.values())

        # 1. loop through strings
        # 2. for each string, string to char array
        # 3. idea: strings in the same anagram group, have the same char list
        # 4. 
