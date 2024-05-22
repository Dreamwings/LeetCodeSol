class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        
        ## S1: Binary Search
        ## T: O(NlogN)
        ## S: O(N)

        # There are n * (n + 1) // 2 subarrays in total.
        # at_most(k) is sliding window algo to find out the number 
        # of subarray with at most k different numbers.

        # Binary search the smallest k that statify:
        # at_most(k) >= total - at_most(k)
        # Then k in the median based on the definition.

        n = len(nums)
        total = n * (n + 1) // 2

        def at_most(k):
            res = 0
            d = Counter()
            i = 0
            for j in range(n):
                d[nums[j]] += 1
                while len(d) > k:
                    d[nums[i]] -= 1
                    if d[nums[i]] == 0:
                        del d[nums[i]]
                    i += 1
                res += j - i + 1
            return res

        lo, hi = 1, len(set(nums))
        while lo < hi:
            k = (lo + hi) // 2
            if at_most(k) * 2 >= total:
                hi = k
            else:
                lo = k + 1
        return lo
