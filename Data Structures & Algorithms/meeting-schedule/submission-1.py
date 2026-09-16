"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        from collections import defaultdict
        meets = defaultdict(int)

        for interval in intervals:
            meets[interval.start] += 1
            meets[interval.end] -= 1
        
        count = 0
        for time in sorted(meets):
            count += meets[time]
            if count > 1:
                return False

        return True