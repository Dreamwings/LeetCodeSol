class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
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

        """
        while lo <= hi :
            m = (lo + hi) // 2
            if m == 0 and nums[m] > nums[m+1]:
                return m
            elif m == n-1 and nums[m] > nums[m-1]:
                return m
            elif nums[m-1] < nums[m] > nums[m+1]:
                return m
            elif nums[m] < nums[m+1]:
                lo = m + 1
            else:
                hi = m - 1
        
        return -1
        """
        
