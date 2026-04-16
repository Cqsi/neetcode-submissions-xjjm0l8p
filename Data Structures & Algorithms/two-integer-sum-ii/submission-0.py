class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        res = []
        i = 0
        j = l-1
        while not res:
            if numbers[i]+numbers[j] > target:
                j -= 1
            elif numbers[i]+numbers[j] < target:
                i += 1
            else:
                res = [i+1, j+1]

        return res