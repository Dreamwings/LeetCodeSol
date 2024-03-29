class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        ## S2: Two Pointers from the End

        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            # note while condition must be m > 0 and n > 0 because 
            # we use index m - 1 and n - 1, so m - 1 >= 0, n - 1 >= 0 
            
        if n > 0: nums1[:n] = nums2[:n]
            
        """

        ## S1: Three Pointers from the End

        if n == 0: return nums1
        if m == 0: nums1[:] = nums2[:]
        
        i, j, k = m-1, n-1, m+n-1
        
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            
        if j >= 0: nums1[:k+1] = nums2[:j+1]
        
        """
                