class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                return n
            else:
                s.add(n)