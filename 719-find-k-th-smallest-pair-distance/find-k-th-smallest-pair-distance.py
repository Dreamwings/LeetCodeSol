class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        ## S2: Binary Search
        ## T: O(NlogN + NlogM), M = max_dist
        ## S: O(1)

        # Count the case there are less than the guess dist
        def less_than(dist: int) -> int:
            i, pairs = 0, 0
            for j in range(len(nums)):
                while nums[j] - nums[i] > dist:
                    i += 1
                pairs += j - i
            return pairs

            nums.sort()
            low, high = 0, nums[-1] - nums[0]
            while low < high:
                mid = low + (high - low) // 2
                # If 'mid' did not produce enouh results, let's increase the guess space 
                if less_than(mid) < k:
                    low = mid + 1
                # If 'mid' did not produce k or more results, it's the upper bound
                else:
                    high = mid
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