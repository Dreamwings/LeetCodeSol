class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:

        ## S2: Min Heap + Max Heap
        ## T: O(NlogN)
        ## S: O(N)

        from heapq import heappush, heappop

        sorted_arr = sorted((nums[i], i) for i in range(len(nums)))
        min_heap, max_heap = [], []
        res = float('inf')

        for i in range(len(sorted_arr)):
            val, index = sorted_arr[i]
            # min heap. smallest indices pop off (look for match on left side)
            heappush(min_heap, (index, val)) 
            # max heap. biggest indices pop off (look for match on right side)
            heappush(max_heap, (-index, val)) 

            # because of sorting, everything in either heap is already less than val. 
            # so we just need to do an index check
            # min_heap we use to check whether current number can be the front half
            while min_heap and min_heap[0][0] + x <= index:
                res = min(res, val - heappop(min_heap)[1])
            # max_heap we use to check whether current number can be back half 
            while max_heap and max_heap[0][0] + x <= -index: 
                res = min(res, val - heappop(max_heap)[1])
            # note that we don't mind popping these off, because we are always checking 
            # their distance with the closest valid partner
        return res   


        
        ## S1: SortedList + Binary Search
        ## T: O(NlogN)
        ## S: O(x) -> O(1) if x doesn't scale with N

        from sortedcontainers import SortedList
        from bisect import bisect_left

        # Create a SortedList to store the current window of numbers
        sorted_arr = SortedList()
        # Initialize the answer with infinity, representing a large number
        res = float('inf')

        # Start iterating from x to the end of the list
        for i in range(x, len(nums)):
            # Add the (current index - x)th element to maintain the window
            sorted_arr.add(nums[i - x])
            # Find the index in the sorted list where nums[i] would fit
            j = bisect_left(sorted_arr, nums[i])
          
            # If there is an element on the right, update res
            if j < len(sorted_arr):
                res = min(res, sorted_arr[j] - nums[i])
            # If there is an element on the left, update res
            if j > 0:
                res = min(res, nums[i] - sorted_arr[j - 1])

        # Return the minimum absolute difference found
        return res  
