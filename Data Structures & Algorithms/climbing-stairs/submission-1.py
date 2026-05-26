class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = [0] * (n+1)

        def rec(k):

            if k==0 or k==1:
                return 1
            if memo[k] == 0:
                memo[k] = rec(k-1)+rec(k-2)
            
            return memo[k]

        return rec(n)