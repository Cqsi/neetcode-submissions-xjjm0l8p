class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n+1)]

        # First, we fill up the first column
        # = the ways to make amount 0
        # -> it will be 1 for all options of coins

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):

            coin = coins[i-1]

            for a in range(1, amount + 1):

                # NO: We don't use the current coin
                dp[i][a] = dp[i-1][a]

                # YES: We use the current coin
                if coin <= a:
                    dp[i][a] += dp[i][a-coin]

        # Answer will be in the bottom right corner
        return dp[n][amount]