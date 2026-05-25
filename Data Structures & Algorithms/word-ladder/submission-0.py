class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # this is an undirected graph problem
        # Idea:
        # 1. Make a graph out of the word list (how??)
        #   1.1. Using a hashmap right?
        # 2. Traverse it and check whether beginword and endword are in the same component
        #   2.1. Furthermore it's a BFS problem probably because we are asked to find the minimum amount of steps

        # The answer to (1) is a solution in O(n) using generic wildcard patterns

        h = {}

        for word in wordList:
            for i in range(len(word)):
                wildcard = word[:i] + "*" + word[i+1:]
                if wildcard in h:
                    h[wildcard].append(word)
                else:
                    h[wildcard] = [word]

        visit = set()
        visit.add(beginWord)
        q = collections.deque()
        q.append(beginWord)
        steps = 1

        while q:
            
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return steps
                for j in range(len(word)):
                    wildcard = word[:j] + "*" + word[j+1:]
                    if wildcard in h:
                        for neiWord in h[wildcard]:
                            if neiWord not in visit:
                                visit.add(neiWord)
                                q.append(neiWord)
            steps+=1
        
        return 0



