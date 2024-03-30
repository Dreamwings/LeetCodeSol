class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
                
        from bisect import bisect_left, bisect_right

        ## S1: Binary Search
        
        n = len(nums)
        if n == 0: return [-1, -1]
        if target < nums[0] or target > nums[-1]: return [-1, -1]
        
        i = bisect_left(nums, target)
        if nums[i] != target: return [-1, -1]
        # now we make sure target in nums
        j = bisect_right(nums, target)
        
        return [i, j-1]

        """
        ## S2: Binary Search
        
        if not nums: return [-1, -1]
        
        def bi_search(arr, x):
            lo, hi = 0, len(arr) - 1
            while lo <= hi:
                m = (lo + hi) >> 1
                if arr[m] >= x:
                    hi = m - 1
                else:
                    lo = m + 1
            return lo
        
        
        lo = bi_search(nums, target)
        if lo >= len(nums) or nums[lo] != target: 
            return [-1, -1]
        else:
            hi = bi_search(nums, target + 1)
            return [lo, hi - 1]
        """
        