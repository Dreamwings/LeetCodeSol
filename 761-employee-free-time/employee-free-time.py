"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        # Flattening the schedule
        intervals = [interval for employee in schedule for interval in employee]
        # Sorting by start of each Interval
        intervals.sort(key=lambda x: x.start)
        
        res = []
        end = intervals[0].end

        for i in intervals[1:]:
            # Checks if the previous end is smaller than the current start
            if i.start > end:
                res.append(Interval(end, i.start))
            end = max(end, i.end)

        return res    