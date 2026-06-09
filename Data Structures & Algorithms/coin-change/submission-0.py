class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # We have a 2D-array because our memoization depends on two factors:
        # - amount
        # - n which is the number of coins that is included
        memo = [-2] * (amount+1)

        def dp(a: int) -> int:

            if a == 0:
                return 0
            
            if a < 0:
                return float('inf')

            if memo[a] != -2:
                return memo[a]

            memo[a] = min(dp(a-coin)+1 for coin in coins)
            return memo[a]
        
        answer = dp(amount)
        return -1 if answer == float('inf') else answer


        