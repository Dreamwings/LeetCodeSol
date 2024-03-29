class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter
        from heapq import nlargest, heappush, heappop

        
        ## S4: Bucket sort
        ## T: O(N)
        ## S: O(N)
        
        d = Counter(nums) # O(N)
        n = max(d.values())
        bucket = [[] for _ in range(n + 1)]
        res = []

        # O(N)
        for x, f in d.items(): 
            bucket[f].append(x)
        
        # O(N)
        for f in range(n, -1, -1):
            res += bucket[f]
            k -= len(bucket[f])
            if k <= 0:
                break

        return res

        """
        
        ## S3: dict.most_common(k)
        ## T: O(NlogK)
        ## S: O(N)
        
        d = Counter(nums).most_common(k)
        return [x for x, f in d]
        
        
        ## S2: Heapq.nlargest
        ## T: O(NlogK)
        ## S: O(N)

        d = Counter(nums)
        freq = [(f, x) for x, f in d.items()]
        res = []
        
        for f, x in nlargest(k, freq):
            res.append(x)
            if len(res) == k:
                break
        return res

        
        
        ## S1: Heapq
        ## T: O(NlogK)
        ## S: O(N)

        d = Counter(nums)
        res = []
        for x, f in d.items():
            heappush(res, (f, x))
            if len(res) > k:
                heappop(res)

        return [x for f, x in res]
        """
