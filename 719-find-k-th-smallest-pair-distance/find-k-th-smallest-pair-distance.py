class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        ## S2: Binary Search
        ## T: O(NlogN + NlogM), M = max_dist
        ## S: O(1)

        # Return if there are k or more pairs with distance <= guess
        def possible(guess_dist):
            i = count = 0            
            for j in range(len(nums)):
                # If the distance calculated from j-i is less than the guess, decrease the guess window
                while nums[j] - nums[i] > guess_dist:
                    i += 1
                # Count all places between j and i
                count += j - i
            return count >= k

        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = low + (high - low) // 2
            # If 'mid' produces k or more results, it's the upper bound
            if possible(mid):
                high = mid
            # If 'mid' did not produce enouh results, let's increase the guess space 
            else:
                low = mid + 1
        return low


        

        ## S1: Binary Search
        ## T: O(NlogN + NlogM), M = max_dist
        ## S: O(N)

        from bisect import bisect_left

        nums.sort()  # O(NlogN), First, sort the numbers to make it easier to find pairs

        # Helper function to count the number of pairs with distance less than or equal to 'dist'
        def count_pairs_with_max_distance(dist): # O(N)
            count = 0
            # Iterate over the sorted list of numbers
            for i, upper_bound in enumerate(nums):
                # Find lower bound such that upper_bound - lower_bound <= dist
                lower_bound = upper_bound - dist
                # Find the first position where lower_bound can be inserted to maintain sorted order
                insert_pos = bisect_left(nums, lower_bound, 0, i)
                # Accumulate the count of pairs where the distance is less than or equal to 'dist'
                count += i - insert_pos
            return count

        # The maximum possible distance is the difference between the largest and smallest numbers
        max_dist = nums[-1] - nums[0]
      
        # Binary search for the smallest distance such that there are at least 'k' pairs with that distance or less
        # The search is conducted over the range of possible distances
        min_dist = bisect_left(range(max_dist + 1), k, key=count_pairs_with_max_distance)
      
        return min_dist

        