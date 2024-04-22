class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        
        ## S1: SortedList + Sliding Window

        from sortedcontainers import SortedList
        import bisect

        n = len(nums)
        sorted_list = SortedList() # a sorted list to maintain a sorted order of numbers
        min_cost = float("inf")
        i = 1 # left pointer of sliding window
        cur_sum = 0 # Running sum of the k-1 elements

        for j in range(1, n):
            # Find the position where nums[j] should be inserted
            insert_pos = bisect.bisect_left(sorted_list, nums[j])
          
            # Add the current number to the sorted list
            sorted_list.add(nums[j])

            # If the insert position is less than k - 1, update the running sum
            if insert_pos < k - 1:
                cur_sum += nums[j]
                # If the sorted list has more than k - 1 elements, subtract the k-th element
                if len(sorted_list) > k - 1:
                    cur_sum -= sorted_list[k - 1]

            # If the window size is larger than allowed by 'dist', adjust the window from the i
            while j - i > dist:
                # Find the index of the i-most number to be removed
                removed_index = sorted_list.index(nums[i])
                # Remove the i-most element
                removed_num = nums[i]
                sorted_list.remove(removed_num)

                # Adjust the running sum based on the position of the removed element
                if removed_index < k - 1:
                    cur_sum -= removed_num
                    # If there are still at least k - 1 elements, add the (k-1)-th element to the running sum
                    if len(sorted_list) >= k - 1:
                        cur_sum += sorted_list[k - 2]
                # Move the i window index to the right
                i += 1

            # If the window size is at least k - 1, calculate the cost to consider this subarray
            if j - i + 1 >= k - 1:
                min_cost = min(min_cost, cur_sum)

        # Return the minimum cost added with the first element that was set aside
        return min_cost + nums[0]
