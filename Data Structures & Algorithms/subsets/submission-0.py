class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def subsetRecursion(i, arr, res, subset):
            if i == len(arr):
                res.append(subset[:])
                return
            
            subset.append(arr[i])
            subsetRecursion(i + 1, arr, res, subset)

            subset.pop()
            subsetRecursion(i + 1, arr, res, subset)

            return res
        
        return subsetRecursion(0, nums, [], [])