class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        ## S1: Sliding Window
        ## T: O(N)
        ## S: O(N)

        # Count the number of ones in the list
        count_of_ones = nums.count(1)
        n = len(nums)
      
        # Create an extended sum list which is twice the length of the nums list plus one
        # This is for the purpose of creating a sliding window later on
        pre_sum = [0] * ((n << 1) + 1)
      
        # Fill the sum list with prefix sums, allowing wrap around to simulate a circular array
        for i in range(n << 1):
            pre_sum[i + 1] = pre_sum[i] + nums[i % n]
      
        # Initialize max_ones_found variable as 0
        max_ones_found = 0
      
        # Iterate through the pre_sum array to find the maximum number of ones in any subarray
        # of the size count_of_ones, which is the number of swaps needed on a circular array
        for i in range(n << 1):
            end = i + count_of_ones - 1
            if end < (n << 1):
                # Update max_ones_found with the maximum ones found in the current sliding window
                max_ones_found = max(max_ones_found, pre_sum[end + 1] - pre_sum[i])
      
        # The minimum number of swaps needed is the total one count minus the maximum ones found
        return count_of_ones - max_ones_found