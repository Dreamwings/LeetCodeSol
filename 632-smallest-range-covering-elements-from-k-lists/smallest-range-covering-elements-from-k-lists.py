class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        from heapq import heapify, heappush, heappop
        
        ## S2: Heap
        ## T: O(N*logM), M = len(nums), N is the total number of all values from all the lists
        ## S: O(M)

        # Create a heap and initialize it with the first element from each of the k lists.
        hp = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapify(hp)

        max_val = max(row[0] for row in nums)
        lo, hi = float('-inf'), float('inf')
        
        # While the heap has elements from each list:
        # a. Pop the smallest element from the heap.
        # b. If the range from the maximum element minus the popped element is 
        #    smaller than the current range:
        #    Update the lo and hi variables.
        # c. If there is another element in the list from which we just popped:
        #    Get the next element and add it to the heap.
        #    Update the max_val variable if necessary.
        while len(hp) == len(nums):
            val, r, c = heappop(hp)
            if max_val - val < hi - lo:
                lo, hi = val, max_val
            if c + 1 < len(nums[r]):
                next_val = nums[r][c + 1]
                max_val = max(max_val, next_val)
                heappush(hp, (next_val, r, c + 1))
                
        return [lo, hi]
        


        """

        ## S1: Sorting
        ## T: O(NlogN)
        ## S: O(N)

        # Flatten the list of lists with their originating list's index
        flat_list = [(value, idx) for idx, sublist in enumerate(nums) for value in sublist]
        flat_list.sort()  # Sort the list of tuples by the numeric value
      
        # Counter to maintain the number of times an element from each list appears in the range
        count = Counter()
        res = [float('-inf'), float('inf')]
        k = 0 # Pointer to iterate the flattened list
       
        for r_val, origin_idx in flat_list:
            # Increase the count for the current list index
            count[origin_idx] += 1
          
            # If the current range includes at least one element from each list
            while len(count) == len(nums):
                # Get the left bound of the current range
                l_val = flat_list[k][0]
                # Calculate the size difference from the best range found so far
                size_diff = r_val - l_val - (res[1] - res[0])
                # Update the res if the current range is smaller, or equally small but starting with a smaller value
                if size_diff < 0 or (size_diff == 0 and l_val < res[0]):
                    res = [l_val, r_val]
                # Get the list index of the left bound of the current range
                left_origin_index = flat_list[k][1]
                # Decrease the count for this list index
                count[left_origin_index] -= 1
                # If count reaches zero, it means we no longer have an element from this list in range
                if count[left_origin_index] == 0:
                    # Remove it from count
                    count.pop(left_origin_index)
                # Move the left k forward
                k += 1
      
        # Return the final smallest range found
        return res

        """
