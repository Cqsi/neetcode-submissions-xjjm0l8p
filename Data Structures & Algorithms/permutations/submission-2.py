class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) <= 1:
            return [nums]

        result = []

        for i, val in enumerate(nums):
            rest = nums[:i] + nums[i+1:]
            for p in self.permute(rest):
                result.append([val] + p)
            
        return result