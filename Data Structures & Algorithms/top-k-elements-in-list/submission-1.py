class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # O(n) solution!
        
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        result = []

        # make a count dictionary
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # make a frequency array, add the numbers to the frequency index
        # that had the specific frequency (it can be many elements)
        for n, c in count.items():
            freq[c].append(n)

        # loop backwards through the frequency array, therefore no need for sorting
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result


        
