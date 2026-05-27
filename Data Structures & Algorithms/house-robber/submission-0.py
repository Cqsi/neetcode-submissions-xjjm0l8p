class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # At each index we have:
        # nums[i] = max(nums[i+2], nums[i+3])

        nums = nums + [0, 0, 0]

        for i in range(len(nums)-5, -1, -1):
            nums[i] += max(nums[i+2], nums[i+3])

        return max(nums[0], nums[1])
        
        