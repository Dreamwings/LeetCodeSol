class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        ## S1: Greedy
        ## T: O(NlogN)
        ## S: O(N)

        # To keep intervals as more as possible, consider "end" time.
        # k is the most recent previous "end" time, current "start" >= k to avoid intervals
        # Minimize k, so that we keep max number of intervals.
        # ==> Sorting by "end" time.
        intervals.sort(key = lambda x: x[1]) # Sorting by "end"
        
        ans = 0
        k = -inf
        
        for x, y in intervals:
            if x >= k:
                # Case 1
                k = y
            else:
                # Case 2
                ans += 1
        
        return ans