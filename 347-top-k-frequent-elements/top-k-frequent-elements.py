class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter
        from heapq import nlargest, heappush, heappop

        ## S6: Bucket sort
        ## T: O(N), no elem freq can be larger than N.
        ## S: O(N)
        
        d = Counter(nums) # O(N)
        max_freq = max(d.values()) # max freq
        bucket = [[] for _ in range(max_freq + 1)]
        
        # O(N)
        for x, f in d.items(): 
            bucket[f].append(x)
        
        # O(N)
        res = [x for arr in bucket for x in arr]

        return res[::-1][:k]


        ## S5: Bucket sort
        ## T: O(N), no elem freq can be larger than N.
        ## S: O(N)
        
        d = Counter(nums) # O(N)
        max_freq = max(d.values()) # max freq
        bucket = [[] for _ in range(max_freq + 1)]
        res = []

        # O(N)
        for x, f in d.items(): 
            bucket[f].append(x)
        
        # O(N)
        for f in range(max_freq, -1, -1):
            res += bucket[f]
            k -= len(bucket[f])
            if k <= 0:
                break

        return res


        ## S4: Quick Select Sorting
        ## T: O(N) on avg, O(N^2) for the worst case
        ## S: O(N)

        d = Counter(nums) # O(N)

        def quick_select(arr, K):
            # Function to sort arr and return the K largest element
            # arr = list(d.items()), each elem of arr is (val, freq) pair
            # This func is sorting according to "freq" of each elem

            pivot = random.choice(arr)[1] # random choice of a freq value
            sm, eq, gt = [], [], []

            for x, f in arr:
                if f < pivot:
                    sm.append((x, f))
                elif f > pivot:
                    gt.append((x, f))
                else:
                    eq.append((x, f))
            len_gt, len_eq = len(gt), len(eq)
            if K <= len_gt:
                return quick_select(arr, K)
            elif K > len_gt + len_eq:
                return gt + eq + quick_select(sm, K - len_gt - len_eq)
            else:
                return gt + eq
        
        k_frequent = quick_select(list(d.items()), k)
        return [x for x, f in k_frequent]

        
        ## S1: dict.most_common(k)
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

        
        
        ## S3: Heapq
        ## T: O(NlogK)
        ## S: O(N+K)

        d = Counter(nums)
        res = []
        for x, f in d.items():
            heappush(res, (f, x))
            if len(res) > k:
                heappop(res)

        return [x for f, x in res]

