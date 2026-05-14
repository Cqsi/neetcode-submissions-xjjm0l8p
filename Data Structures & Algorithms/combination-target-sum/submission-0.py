class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.res = []

        def track(i, cur, sm):
            
            if i == len(nums):
                return  
            
            cur.append(nums[i])
            sm += nums[i]

            if sm == target:
                self.res.append(cur[:])
            elif sm < target:
                track(i, cur, sm)

            cur.pop()
            sm -= nums[i]
            track(i+1, cur, sm)

        track(0, [], 0)
        return self.res
