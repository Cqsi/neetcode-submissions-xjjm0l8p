from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # O(n) solution
        # It's rather obvious from the question that we will use a sliding window
        # with a left and right pointer. It's easy to also check once we increase
        # the right pointer whether the new elemenet is larger than the current max.
        
        # The problem is when the current max goes out from the current window,
        # when the left pointer increases. How can we represent this data?

        # For an O(nlogk) solution I believe the answer is Priority Queue, but for our O(n)
        # solution we have the possibility to use a deque.

        # It will be a monotonically decreasing queue which is based on the fact that 
        # if a new max appears, then we can discard all of the earlier elements

        # Also another thing to realize is that q stores indices.

        output = []

        # q will store indices!
        q = deque()
        l = r = 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # removal left val from window
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1

        return output