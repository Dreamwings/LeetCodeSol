class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        ## S1:
        
        # the left most val of the k integers must in arr[:n-k]
        # do binary search
        
        n = len(arr)
        l, r = 0, n - 1 - k
        
        while l <= r:
            m = (l + r) >> 1
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m - 1
        
        return arr[l : l+k]
        """

        ## S2:

        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
          
            # Check the distance from the x to the middle element and the element at mid + k position.
            # If the element at mid is closer to x or equal in distance compared to the element at mid + k,
            # we move the right pointer to mid. Otherwise, we adjust the left pointer to mid + 1.
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
      
        return arr[left:left + k]      

        """
         