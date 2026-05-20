class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # Basic idea:
        # 1. Do a check function that checks if we can place queen at row r in position i
        # 2. Use a backtracking function with a for loop for looping through the indices
        # Define the board and result outside everything, pop the board once the backtracking recursion is done
        
        board = []
        res = []

        if n == 1:
            return [["Q"]]
        elif n == 2 or n == 3:
            return []

        def check(col) -> bool:
            rows = len(board)
            
            for r in range(rows):
                # same column
                if board[r][col] == "Q":
                    return False

                d = rows - r

                # upper-right diagonal
                if col+d < n and board[r][col+d] == "Q":
                    return False

                # upper-left diagonal
                if col-d >= 0 and board[r][col-d] == "Q":
                    return False

            return True
        

        def backtrack(row):

            if row == n:
                res.append(board.copy())
                return

            # smart code:
            # 1. We append rows to board
            # 2. When we are row == n we append the current board
            # 3. Then after each backtrack call we 
            for col in range(n):
                if check(col):
                    row_string = "." * col + "Q" + "." * (n - col - 1)
                    board.append(row_string)
                    
                    # backtracking
                    backtrack(row + 1)
                    board.pop()
                    
        backtrack(0)
        return res
            

