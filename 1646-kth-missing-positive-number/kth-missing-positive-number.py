class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        ## S1: Binary Search
        ## T: O(logN)
        ## S: O(1)

        l, r = 0, len(arr) - 1
        
        while l <= r:
            m = (l + r) >> 1
            if arr[m] - (m + 1) < k:
                l = m + 1
            else:
                r = m - 1
        
        return l + k
        