from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                e = board[r][c]
                if e == ".":
                    continue
                if e in rows[r] or e in cols[c] or e in squares[(r//3, c//3)]:
                    return False
                rows[r].add(e)
                cols[c].add(e)
                squares[(r//3, c//3)].add(e)

        return True
