class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[0])
        kept = []

        for interval in intervals:
            if kept and interval[0] < kept[-1][1]:
                if interval[1] < kept[-1][1]:
                    kept[-1] = interval
            else:
                kept.append(interval)
        
        return len(intervals) - len(kept)