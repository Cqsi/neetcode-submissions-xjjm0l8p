class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # usually we do something like lastChar: bool, but 
        # here it makes sense to store the actual word in the TrieNode, to avoid
        # having to keep track of the whole word in the solution below

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Trie Data Structure
        # https://www.geeksforgeeks.org/dsa/trie-insert-and-search/

        rows = len(board)
        cols = len(board[0])

        # Trie implementation
        root = TrieNode()

        for w in words:
            # we go back to the root
            cur = root 

            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = w
        
        res = []
        path = set()

        def dfs(r, c, node):

            # 1. invalid position / already visited
            if r not in range(rows) or c not in range(cols) or (r, c) in path:
                return

            ch = board[r][c]

            # 2. current character cannot continue this trie path
            if ch not in node.children:
                return

            # 3. move into the trie child
            node = node.children[ch]
            
            # 4. Check whether this completes a word
            if node.word:
                res.append(node.word)
                node.word = None

            # 5. Continue with DFS
            path.add((r,c))

            dfs(r+1, c, node)
            dfs(r-1, c, node)
            dfs(r, c+1, node)
            dfs(r, c-1, node)

            path.remove((r, c))
        
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res

        