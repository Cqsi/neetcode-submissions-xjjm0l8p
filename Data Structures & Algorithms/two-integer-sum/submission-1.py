class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {} # number -> index

        for i, n in enumerate(nums):
            c = target - n
            if c in seen:
                return [seen[c], i]
            seen[n] = i  