class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 == 1:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        # Basic of DP approach: we can either include or not include a number
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for d in dp:
                nextDP.add(d + nums[i])
                nextDP.add(d)
            dp = nextDP
        
        return True if target in dp else False
