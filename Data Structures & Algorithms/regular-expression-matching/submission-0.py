class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # Suffix-based DP:
        # dp[i][j] = whether s[i:] matches p[j:]

        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):

                current_match = (
                    i < m
                    and (s[i] == p[j] or p[j] == ".")
                )

                if j + 1 < n and p[j + 1] == "*":
                    dp[i][j] = dp[i][j+2] or (current_match and dp[i+1][j])
                else:
                    dp[i][j] = (
                        current_match
                        and dp[i + 1][j + 1]
                    )

        return dp[0][0]