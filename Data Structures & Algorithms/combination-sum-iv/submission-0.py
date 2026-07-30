class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def dp(rem):

            if rem == 0:
                return 1
            
            if rem < 0:
                return 0
            
            if rem in memo:
                return memo[rem]
            
            combs = 0

            for num in nums:
                combs += dp(rem-num)
            
            memo[rem] = combs
            return combs
        
        return dp(target)
        
