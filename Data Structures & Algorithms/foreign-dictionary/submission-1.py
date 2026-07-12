class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        graph = {}

        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = set()
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            min_length = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
                return ""
            
            for j in range(min_length):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break

        visit = set()
        path = set()
        res = []

        def dfs(char):

            if char in path:
                return False

            if char in visit:
                return True

            path.add(char)

            for nei in graph[char]:
                if not dfs(nei):
                    return False
            
            path.remove(char)
            visit.add(char)
            res.append(char)
            return True

        # why call this for every char?
        for char in graph:
            if not dfs(char):
                return ""

        res.reverse()
        return "".join(res)
