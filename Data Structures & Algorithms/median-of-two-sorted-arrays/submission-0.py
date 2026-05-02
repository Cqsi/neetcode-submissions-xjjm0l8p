class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Wte are given two sorted arrays
        # We need to return the median value among all the elements of the two arrays
        # supposedly using binary search

        # Idea 1: We could get their combined length and somehow
        # ok wow, that is O(n+m) i guess, how tf do we get log(n+m)??

        # It must have something to do with "choosing one element in one of the arrays" and
        # and then finding the element in the other array
        
        # ex. [1,2,3,4,5,6] and [8,9] (1)
        # ex. [1,4,5,6,9] and [3,4,5] (2)
        
        # Does the bigger array "lead" the median calc?
        # in (1) we get that the median is just shifted in the first array
        # [1,2,3,4,5,6,8,9] -> m = (4+5)/2=4.5 from before (3+4)/2=3.5

        # 1. take the bigger array
        # 2. find the middle value(s) of shit, what happens when they are nearly the equal lenght?
        # 3. Check

        # ABOVE IS ALL WRONG (!)

        # m = len(nums1)
        # n = len(nums2)
        #half = (n+m)//2
         
        # x is between these two values
        #lo = 0
        #hi = min(n,m)-1

        #whi#le lo <= hi:
            #x = (lo+hi)//2

            #if nums1[x-1] > nums2[hi-x]:
            #    hi = x-1
            #elif nums1[x] < nums2[hi-x-1]:
            #    lo = x+1
            #else:
            #    if (m+n)%2 == 0:
            #        return (max(nums1[x-1], nums2[hi-x-1]) + min(nums1[x], nums2[hi-x]))/2
            #    else:
            #        return max(nums1[x-1], nums2[hi-x-1])

        # A will be the smaller array
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2
        
        lo = 0
        hi = len(A) - 1

        while True:
            i = (lo + hi) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if (i+1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf")

            # Our two conditions for the partition being correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                hi = i - 1
            else:
                lo = i + 1