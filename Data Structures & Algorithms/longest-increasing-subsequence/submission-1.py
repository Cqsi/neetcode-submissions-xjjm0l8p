class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def LISending(nums, idx, dp):

            if idx == 0:
                return 1
            
            if dp[idx] != -1:
                return dp[idx]
            
            maxLen = 1
            for prev in range(idx):
                if nums[prev] < nums[idx]:
                    maxLen = max(maxLen, 1 + LISending(nums, prev, dp))
            
            dp[idx] = maxLen
            return dp[idx]

        
        n = len(nums)
        dp = [-1] * n

        res = 1
        for idx in range(1, n):
            res = max(res, LISending(nums, idx, dp))
        return res