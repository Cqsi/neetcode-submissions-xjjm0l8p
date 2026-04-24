class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # Idea:
        # 1. We use binary search. However we can't directly based on the middle
        # value choose which half to choose
        # 2. How do we know whether to pick the left or right part? We could
        # check the last element in the left and right array?
        # ex. [4,5,1,2,3] we check last element in left array (5?) against 3, so we
        # know the minimum is in the right array
        # ex 2. [5,1,2,3,4] works as well

        lo = 0
        hi = len(nums)-1

        while lo<hi:
            # ex1 -> 2
            m = (lo+hi)//2

            if nums[m]>nums[hi]:
                lo = m+1
            else:
                hi = m
        
        return nums[lo]