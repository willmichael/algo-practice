# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)
        if len(intervals) < 1:
            return intervals
        i = 0
        while i < len(intervals)-1:
            if len(intervals) < 2:
                return intervals
            elif intervals[i].start == intervals[i+1].start:
                # Grab larger interval range
                if intervals[i].end < intervals[i+1].end:
                    intervals.pop(i)
                else:
                    intervals.pop(i+1)
            elif intervals[i].end >= intervals[i+1].start:
                # Merge intervals
                if intervals[i].end > intervals[i+1].end:
                    intervals.pop(i+1)
                else:
                    intervals.insert(i, Interval(intervals[i].start, intervals[i+1].end))
                    intervals.pop(i+1)
                    intervals.pop(i+1)
            else:
                i += 1
        return intervals
