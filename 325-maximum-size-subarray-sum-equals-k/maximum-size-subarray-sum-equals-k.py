class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        ## S1: Hashmap 

        # Initialize a dictionary to store the cumulative sum up to all indices
        d = {0: -1} # pre_sum: index
      
        # Initialize variables to store the maximum length of subarray and the cumulative sum
        max_length = pre_sum = 0
      
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Update the cumulative sum
            pre_sum += num
          
            # Check if there is a subarray whose sum equals 'target'
            if (pre_sum - k) in d:
                # Update max_length with the larger of the previous max_length and the current subarray length
                max_length = max(max_length, i - d[pre_sum - k])
          
            # If this cumulative sum has not been seen before, add it to the dictionary
            if pre_sum not in d:
                d[pre_sum] = i
      
        # Return the maximum length of subarray found that adds up to 'target'
        return max_length

        