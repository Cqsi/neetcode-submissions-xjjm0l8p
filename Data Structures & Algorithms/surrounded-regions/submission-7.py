class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows = len(board)
        cols = len(board[0])
        visit = set()

        def dfs(row, col):

            if board[row][col] == "O":
                visit.add((row, col))
            else:
                return
            
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if r in range(rows) and c in range(cols) and board[r][c] == "O" and (r,c) not in visit:
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows-1 or c == cols-1:
                    dfs(r,c)

        print(visit)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visit:
                    board[r][c] = "X"