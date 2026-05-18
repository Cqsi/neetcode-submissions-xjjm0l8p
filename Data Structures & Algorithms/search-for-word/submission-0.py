class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # x = len(board[0])
        # y = len(board)

        # self.res = False

        # def loop(cur, i, j, back): # i = x pos, j = y pos

        #     print(i, j)

        #     if cur == word:
        #         self.res = True
        #         return
            
        #     if i == x-1 and j == y-1:
        #         return
        
        #     if board[j][i] == word[len(cur)]:
        #         cur += board[j][i]
        #         if i < x-1:
        #             loop(cur, i+1, j, False)
        #         if j < y-1:
        #             loop(cur, i, j+1, False)
        #         if i>0:
        #             loop(cur, i-1, j, True)
        #         if j>0:
        #             loop(cur, i, j-1, True)
        #     else:
        #         if back:
        #             return 
        #         else:
        #             cur = ""
        #             if i < x-1:
        #                 loop(cur, i+1, j, False)
        #             if j < y-1:
        #                 loop(cur, i, j+1, False)

        # return loop("", 0, 0, False)

        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            # The if->false statement is quite extensive. We have to check for
            # - if r and c are out of bounds
            # - if current char on the board is not equal to the word char
            # - if current (r,c) has already been visited
            if (r < 0 or c < 0 or r >= rows or
                c >= cols or word[i] != board[r][c]
                or (r, c) in path):
                return False
            
            path.add((r, c))
            res = (dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1))
            path.remove((r, c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
            
        return False



