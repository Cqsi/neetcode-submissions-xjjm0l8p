class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        # we are doing backwards
        # dp[i] = the best score difference the current player 
        # can achieve starting at index i
        # If the difference is negative, cur player loses. If it's 0 then it's a tie etc
        n = len(stoneValue)
        dp = [0] * (n+1)
        dp[n] = 0

        for i in range(n-1, -1, -1):
            
            total = 0
            best = float('-inf')

            for take in range(1,4):
                if i + take > n:
                    break
                
                total += stoneValue[i+take-1]
                cand = total - dp[i+take]
                best = max(best, cand)
            
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] == 0:
            return "Tie"
        else:
            return "Bob"