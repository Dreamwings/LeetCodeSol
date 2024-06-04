class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        from bisect import bisect, insort
        from heapq import heappush, heappop, heappushpop
        
        
        ## S2: Min Heap and Max Heap (Lazy Removal)
        ## T: O(N logK)
        ## S: O(K)
        
        if not nums or not k:
            return []
        lo = [] # max heap
        hi = [] # min heap
        for i in range(k):
            if len(lo) == len(hi):
                heappush(hi, -heappushpop(lo, -nums[i]))
            else:
                heappush(lo, -heappushpop(hi, nums[i]))
        ans = [float(hi[0])] if k & 1 else [(hi[0] - lo[0]) / 2.0]
        to_remove = defaultdict(int) # Holds the count of the elements delayed for removal
        # In the worst case, this could hold each unique number once, K, assuming the 
        # sliding window could contain up to k unique elements

        for i in range(k, len(nums)): # Right bound of window
            heappush(lo, -heappushpop(hi, nums[i])) # Always push to lo
            out_num = nums[i-k]
            if out_num > -lo[0]:
                heappush(hi, -heappop(lo))
            to_remove[out_num] += 1
            while lo and to_remove[-lo[0]]:
                to_remove[-lo[0]] -= 1
                heappop(lo)
            while to_remove[hi[0]]:
                to_remove[hi[0]] -= 1
                heappop(hi)
            if k % 2:
                ans.append(float(hi[0]))
            else:
                ans.append((hi[0] - lo[0]) / 2.0)
        return ans
        
        

        ## S1: Insort 
        ## T: O(N*K*logK) ~ O(N*K)
        ## S: O(K)

        medians, window = [], []

        for i in range(len(nums)):

            # Find position where outgoing element should be removed from
            if i >= k:
                # window.remove(nums[i-k])        # this works too
                window.pop(bisect(window, nums[i - k]) - 1)  # faster

            # Maintain the sorted invariant while inserting incoming element
            insort(window, nums[i])

            # Find the medians
            if i >= k - 1:
                medians.append(float((window[k // 2]
                    if k & 1 > 0
                    else(window[k // 2 - 1] + window[k // 2]) * 0.5)))

        return medians

        
        
        ## S3: Sort + Insort
        ## Time: O(N*K*logK) 
        ## https://leetcode.com/problems/sliding-window-median/discuss/96337/Python-SortedArray-(beats-100)-and-2-Heap(beats-90)-solution
        
        win, rv = nums[:k], []
        win.sort()
        odd = k%2
        for i,n in enumerate(nums[k:],k):
            rv.append((win[k//2]+win[k//2-1])/2. if not odd else win[(k-1)//2]*1.)
            win.pop(bisect(win, nums[i-k])-1) # <<< bisect is faster than .remove()
            insort(win, nums[i])
        rv.append((win[k//2]+win[k//2-1])/2. if not odd else win[(k-1)//2]*1.)
        return rv
        