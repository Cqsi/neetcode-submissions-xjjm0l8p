import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # We want to find the smallest possible integer k, where k is the
        # bananas-per-hour eating rate.

        # We are going to do binary search on values of k, starting with k=1 and the high
        # as the maximum from the piles. There is no point in having less or higher
        # than that.
        lo = 1 # in this case h = sum(piles)
        hi = max(piles) # in this case h = len(piles)
        # our task is to find the lowest k that is <= h
        # and for this we can use binary search

        while lo<=hi:
            k = (lo+hi)//2
            
            # feels slow but this is O(n) and binary search is O(logn)
            # so the total time complexity is not too bad
            hours = sum(math.ceil(pile/k) for pile in piles)

            if hours <= h:
                hi = k-1
            else:
                lo = k+1
        
        return lo