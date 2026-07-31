class Solution:
    def integerBreak(self, n: int) -> int:

        if n == 2:
            return 1
        
        memo = {}

        def ib(num):

            if num == 1:
                return 1
            
            if num == 2:
                return 2

            if num in memo:
                return memo[num]

            m = 0

            for i in range(1, num):
                remainder = num - i

                m = max(
                    m,
                    i * max(remainder, ib(remainder))
                )
            
            memo[num] = m
            return m
        
        return ib(n)