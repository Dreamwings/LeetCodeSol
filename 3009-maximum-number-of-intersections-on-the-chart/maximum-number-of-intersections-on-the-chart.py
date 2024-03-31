class Solution:
    def maxIntersectionCount(self, y: List[int]) -> int:
        
        ## S1: Sorting, Sweeping Line
        ## T: O(NlogN)
        ## S: O(N)

        dc = {v: 2 * i for i, v in enumerate(sorted(set(y)))}
        y = [dc[v] for v in y]
        ct = Counter(y)
        ma = max(y)
        dif = [0] * (ma + 2)
        for i in range(len(y) - 1):
            mi, ma = min(y[i], y[i + 1]), max(y[i], y[i + 1])
            dif[mi + 1] += 1
            dif[ma] -= 1
        ans = 0
        for i, x in enumerate(accumulate(dif)):
            ans = max(ans, x + ct[i])
        return ans


        """

        ## S2: Sorting + MinHeap


        candles = []
        for idx in range(len(y)-1):
            left = 2*y[idx]
            if idx != 0 and y[idx]<y[idx+1]:
                left += 1
            elif idx!=0 and y[idx]>y[idx+1]:
                left -= 1
            right = 2*y[idx+1]
            candles.append((min(left, right), max(left, right)))
        
        candles.sort()
        heap = [candles[0][1]]
        for idx in range(1, len(candles)):
            if candles[idx][0] > heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, candles[idx][1])
        return len(heap)

        """