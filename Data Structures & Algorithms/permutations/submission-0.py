class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def permutation(arr):

            if len(arr) <= 1:
                return [arr]

            result = []

            for i, val in enumerate(arr):
                rest = arr[:i] + arr[i+1:]
                for p in permutation(rest):
                    result.append([val] + p)
                
            return result
        
        return permutation(nums)