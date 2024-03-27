class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        import collections
        import heapq  

        ## S1: Line Sweep, Heap
        ## T: O(NlogN)
        ## S: O(N)

        points = collections.defaultdict(list)
        for i, (s, e) in enumerate(paint):
            points[s].append((True, i))
            points[e].append((False, i))
        min_heap = []
        lookup = [False]*len(paint)
        result = [0]*len(paint)
        prev = -1
        for pos in sorted(points.keys()):
            while min_heap and lookup[min_heap[0]]:
                heapq.heappop(min_heap)
            if min_heap:
                result[min_heap[0]] += pos-prev
            prev = pos
            for t, i in points[pos]:
                if t:
                    heapq.heappush(min_heap, i)
                else:
                    lookup[i] = True
        return result

        """
        ## S2:
        ## T: O(NlogN)
        ## S: O(N)

        from sortedcontainers import SortedList      

        points = collections.defaultdict(list)
        for i, (s, e) in enumerate(paint):
            points[s].append((True, i))
            points[e].append((False, i))
        sl = SortedList()
        result = [0]*len(paint)
        prev = -1
        for pos in sorted(points.iterkeys()):
            if sl:
                result[sl[0]] += pos-prev
            prev = pos
            for t, i in points[pos]:
                if t:
                    sl.add(i)
                else:
                    sl.remove(i)
        return result

        ## S3:
        ## https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/amount-of-new-area-painted-each-day.py
        """