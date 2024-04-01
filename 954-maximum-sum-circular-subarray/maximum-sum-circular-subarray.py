class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        ## S1:

        max_sum_end_here = min_sum_end_here = max_subarray_sum = min_subarray_sum = nums[0]
      
        # Iterate through the given nums list starting from the second element
        for num in nums[1:]:
            # Update max_sum_end_here to be the maximum of the current number or the current number plus max_sum_end_here
            max_sum_end_here = num + max(max_sum_end_here, 0)
            # Update min_sum_end_here to be the minimum of the current number or the current number plus min_sum_end_here
            min_sum_end_here = num + min(min_sum_end_here, 0)
          
            # Update the max_subarray_sum if the newly computed max_sum_end_here is larger
            max_subarray_sum = max(max_subarray_sum, max_sum_end_here)
            # Update the min_subarray_sum if the newly computed min_sum_end_here is smaller
            min_subarray_sum = min(min_subarray_sum, min_sum_end_here)
      
        # If the max_subarray_sum is non-positive, the whole array could be non-positive
        # Thus, the max subarray sum is the max_subarray_sum itself
        if max_subarray_sum <= 0:
            return max_subarray_sum
        else:
            # Otherwise, we compare the max_subarray_sum vs. total_sum minus min_subarray_sum
            # The latter represents the maximum sum obtained by considering the circular nature of the array
            # We subtract min_subarray_sum from the total sum to get the maximum sum subarray which wraps around the array
            total_sum = sum(nums)
            return max(max_subarray_sum, total_sum - min_subarray_sum)

        """

        ## S2:

        total, maxSum, curMax, minSum, curMin = 0, nums[0], 0, nums[0], 0
        for a in nums:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum

        """
