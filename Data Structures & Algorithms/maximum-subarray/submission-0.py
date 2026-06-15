class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if max(nums) < 0:
            return max(nums)

        l = 0
        r = 0
        maxs = 0
        cur = 0
        while r < len(nums):
            cur+=nums[r]
            if cur < 0:
                l += 1
                cur = 0
            else:
                maxs = max(maxs, cur)
            
            r += 1
        return maxs