class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        dp = {} # longest increase path at a specific grid cell
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(i, j):
            
            if (i, j) in dp:
                return dp[(i, j)]

            longest = 0
            
            for dx, dy in dirs:
                if i+dx in range(m) and j+dy in range(n) and matrix[i+dx][j+dy] > matrix[i][j]:
                    longest = max(longest, dfs(i+dx, j+dy))
            
            dp[(i, j)] = 1 + longest
            return dp[(i, j)]

        longest = 0

        for i in range(m):
            for j in range(n):
                if (i, j) not in dp:
                    dfs(i, j)
                longest = max(longest, dp[(i, j)])
            
        return longest