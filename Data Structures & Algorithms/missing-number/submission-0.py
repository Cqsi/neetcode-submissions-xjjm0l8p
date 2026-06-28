class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        b = 0

        for i in range(len(nums) + 1):
            b ^= i
        
        for n in nums:
            b ^= n
        
        return b
