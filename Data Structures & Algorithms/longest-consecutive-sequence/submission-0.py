class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # idea: we turn nums into a set and then start looping through the set
        # for nums_set[i], if nums_set[i] not in 

        s = set(nums)
        m = 0
        for i in range(len(nums)):
            count = 0
            if nums[i]-1 not in s:
                count = 1
                cur = nums[i]
                while cur+1 in s:
                    cur+=1
                    count+=1
                m = max(m, count)
        
        return m