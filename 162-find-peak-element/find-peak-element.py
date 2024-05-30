class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        ## S1: Binary Search
        ## T: O(logN)
        ## S: O(1)
        
        n = len(nums)
        if n == 1: return 0
        if n == 2:
            if nums[0] > nums[1]: return 0
            else: return 1
        
        lo, hi = 0, n - 1

        while lo < hi:
            m = (lo + hi) // 2
            if nums[m] < nums[m+1]:
                lo = m + 1
            else:
                hi = m
        
        return lo


        
        ## S2: Binary Search (Recursive)
        ## T: O(logN)
        ## S: O(logN)

        def search(l, r):
            if l == r:
                return l
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                return search(l, m)
            return search(m + 1, r)
        
        return search(0, len(nums) - 1)

