class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        rank = {}

        for i, char in enumerate(order):
            rank[char] = i
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            found_diff = False

            for j in range(min(len(word1), len(word2))):

                if word1[j] != word2[j]:
                    found_diff = True

                    if rank[word1[j]] > rank[word2[j]]:
                        return False
                    
                    break

            if not found_diff and len(word1) > len(word2):
                return False
        
        return True