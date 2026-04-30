class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # We need to find an element in a rotated array
        # Examples of rotated array which are two different cases
        # [3,4,5,6,7,1,2] (1)
        # [6,7,1,2,3,4,5] (2)
        # Question is how we differentiate between these and make an algorithm
        # that works for both?

        # IDEA:
        # lo = 0, hi = len(nums)-1
        # m = (lo+hi)//2
        # we take the middle value as usual, but now the question is, how
        # can we ensure we are moving towards the correct value?
        
        # Let's pick left if nums[0] < target < nums[m]
        # otherwise right, doesnt work, consider (2)

        # Let's pick target[m] and if target is less then we check nums[0]
        # against target, if nums[0] > target, then we know its the right,
        # otherwise left

        # if target is more than nums[m] we check nums[l] and if its larger than
        # than target then we pick the right opart, otherwise we pick the left part

        # ex target = 2 (1): 6->right, 1->

        # THIS IDEA WAS WRONG
        # Better idea:
        # let's check which half is sorted, there is always one half that is sorted

        lo = 0
        hi = len(nums)-1

        while lo<=hi:
            m = (lo+hi)//2

            if target == nums[m]:
                return m

            if nums[lo] <= nums[m]:
                if target >= nums[lo] and target < nums[m]:
                    hi = m-1
                else:
                    lo = m+1
            else:
                if target <= nums[hi] and target > nums[m]:
                    lo = m+1
                else:
                    hi = m-1



        return -1
