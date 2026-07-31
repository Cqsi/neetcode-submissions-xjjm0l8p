import math

class Solution:
    def numSquares(self, n: int) -> int:
        
        memo = {0: 0}

        for num in range(1, n + 1):
            b = math.floor(math.sqrt(num))
            ans = num

            for i in range(1, b + 1):
                ans = min(ans, 1 + memo[num - i**2])

            memo[num] = ans
        
        return memo[n]