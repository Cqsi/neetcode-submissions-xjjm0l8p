"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        from collections import defaultdict
        meets = defaultdict(int)

        for interval in intervals:
            meets[interval.start] += 1
            meets[interval.end] -= 1
        
        count = 0
        rooms = 0
        
        for time in sorted(meets):
            count += meets[time]
            rooms = max(rooms, count)
        
        return rooms