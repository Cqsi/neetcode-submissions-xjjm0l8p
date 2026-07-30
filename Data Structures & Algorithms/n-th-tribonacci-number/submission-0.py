class Solution:
    def tribonacci(self, n: int) -> int:
        
        dp = [0, 1, 1]

        for i in range(n-2):
            dp.append(dp[i] + dp[i+1] + dp[i+2])

        return dp[n]