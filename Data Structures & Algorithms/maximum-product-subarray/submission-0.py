class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        curMin = 1
        curMax = 1

        for n in nums:

            if n == 0:
                curMin = 1
                curMax = 1
                continue

            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        
        return res