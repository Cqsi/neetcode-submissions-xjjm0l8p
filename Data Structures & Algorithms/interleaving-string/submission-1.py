class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        m = len(s1)
        n = len(s2)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        print(dp)
        
        for i in range(1, m+1):
            if dp[i-1][0] and s1[i-1] == s3[i-1]:
                dp[i][0] = True
        
        for j in range(1, n+1):
            if dp[0][j-1] and s2[j-1] == s3[j-1]:
                dp[0][j] = True

        for i in range(1, m+1):
            for j in range(1, n+1):
                if (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or (dp[i-1][j] and s1[i-1] == s3[i+j-1]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        
        return dp[m][n]