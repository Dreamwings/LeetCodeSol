"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        from heapq import heappush, heappop

        ## S3: Heap Merge
        ## T: O(NlogK), K is num of employees, N is total num of intervals
        ## S: O(K)

        # Create an iterator using heapq.merge
        it = heapq.merge(*schedule, key=operator.attrgetter('start'))
        res, pre_end = [], next(it).end

        for s in it:
            if s.start > pre_end:
                res.append(Interval(pre_end, s.start))

            pre_end = max(pre_end, s.end)
        
        return res

        ## S2: Min Heap
        ## T: O(NlogK), K is num of employees, N is total num of intervals
        ## S: O(K)

        hq, res = [], []

        # First push the first interval start of each employee into hq
        # (interval.start, employee_idx, interval_idx)
        for i, s in enumerate(schedule):
            heappush(hq, (s[0].start, i, 0))

        _, i, _ = hq[0]
        pre_end = schedule[i][0].end

        while hq:
            start, i, j = heappop(hq)
            # Checks if there is free time
            if start > pre_end:
                res.append(Interval(pre_end, start))
                
            pre_end = max(pre_end, schedule[i][j].end)
            
            # Push the next interval of i-th employee into hq
            k = j + 1 
            if k < len(schedule[i]):
                heappush(hq, (schedule[i][k].start, i, k))
        
        return res



        ## S1: Sorting
        ## T: O(NlogN)
        ## S: O(N) for sorting in Python

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