class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pre = ""
        tester = strs[0]

        for i in range(len(tester)):
            c = tester[i]
            for word in strs:
                if i >= len(word) or c != word[i]:
                    return pre
            pre += c

        return pre