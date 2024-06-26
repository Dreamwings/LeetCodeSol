class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        ## S1: Sorting
        ## T: O(NlogN)
        ## S: O(N)

        a = []
        for start, end in intervals:
            a.append((start, 1))
            a.append((end, -1))
        
        cnt, res = 0, 0

        for t, v in sorted(a):
            cnt += v
            res = max(res, cnt)
        
        return res
        


        ## S2: Bucket Sort
        ## T: O(1000010) -> O(1)
        ## S: O(1000010) -> O(1)

        from itertools import accumulate
        # The range is chosen such that it covers all possible meeting times
        meeting_delta = [0] * 1000010
        
        for start, end in intervals:
            meeting_delta[start] += 1  # Increment for a meeting starting
            meeting_delta[end] -= 1    # Decrement for a meeting ending

        # The `accumulate` function is used to compute the running total of 
        # active meetings at each time
        # "max" to find the maximum number of concurrent meetings
        return max(accumulate(meeting_delta))


        
        ## S3: Heap 
        ## T: O(NlogN) + O(NlogK) ~ O(NlogN)
        ## S: O(N)

        n = len(intervals)
        if n<=1: return n
        heap = []

        for start, end in sorted(intervals): # O(NlogN)
            if heap and start >= heap[0]:
                heapq.heappushpop(heap, end) # O(logK)
            else:
                heapq.heappush(heap, end)
        # Time complexity for the for loop is O(NlogK)
        
        return len(heap)

        