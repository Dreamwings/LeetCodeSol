class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        ## S3: Binary Search
        ## T: O(log(N - K))
        ## S: O(1)
        
        # the left most val of the k integers must in arr[:n-k]
        # do binary search
        
        n = len(arr)
        l, r = 0, n - 1 - k
        
        while l <= r:
            m = (l + r) >> 1
            # Check the distance from the x to the middle element and the element at mid + k position.
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m - 1
        
        return arr[l : l+k]
        


        ## S2:  Binary Search + Sliding Window
        ## T: O(log(N)+K)
        ## S: O(1)

        # Base case
        if len(arr) == k:
            return arr
        
        # Find the closest element and initialize two pointers
        left = bisect_left(arr, x) - 1
        right = left + 1

        # While the window size is less than k
        while right - left - 1 < k:
            # Be careful to not go out of bounds
            if left == -1:
                right += 1
                continue
            
            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        # Return the window
        return arr[left + 1:right]



        ## S1: Sort With Custom Comparator
        ## T: O(Nlog(N) + Klog(K))
        ## S: O(N)

        # Sort using custom comparator
        sorted_arr = sorted(arr, key = lambda num: abs(x - num))

        # Only take k elements
        result = []
        for i in range(k):
            result.append(sorted_arr[i])
        
        # Sort again to have output in ascending order
        return sorted(result)