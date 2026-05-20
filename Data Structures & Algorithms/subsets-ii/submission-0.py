class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        # Compared to the last Subsets exercise we need to sort here
        # in order to detect places where are same consecutive numbers
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res