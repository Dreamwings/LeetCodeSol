class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        ## S1: Binary Search
        ## T: O(logN)
        ## S: O(1)

        ## by arr[i], there are arr[i] - (i+1) missing numbers
        ## let m = arr[i] - (i+1), there are m missing numbers before arr[i]
        ## so we need to find the j-th index, so that before arr[j] it's missing m1 numbers
        ## at arr[j+1], it's missing m2 numbers, k meet m1 <= k < m2

        l, r = 0, len(arr) - 1
        
        while l <= r:
            m = (l + r) >> 1
            # How many positive numbers are missing by index m?
            missing_by_m = arr[m] - (m + 1)
            if missing_by_m < k:
                l = m + 1
            else:
                r = m - 1
        
        return l + k
        # How do we get this result? We should return:
        # arr[l-1] + (k - (arr[l-1] - (l -1 + 1)))
        # = arr[l-1] + k - arr[l-1] + l
        # = l + k
        