class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        ## S1: DP
        ## T: O(N)
        ## S: O(1)

        sum1 = sum2 = sum3 = 0
        max_sum1 = max_sum1_2 = 0
        max_idx_1, max_idx_1_2 = 0, ()
        sum = sum1 + sum2 + sum3
        res = []
      
        # Start iterating over the main array from the point where
        # we could fit three subarrays of length k
        for i in range(k * 2, len(nums)):
            # Add the current element to the running sum of each subarray
            sum1 += nums[i - k * 2]  # sum for the first subarray
            sum2 += nums[i - k]      # sum for the second subarray
            sum3 += nums[i]          # sum for the third subarray
          
            # Check if we have traversed 'k' elements for each subarray
            if i >= k * 3 - 1:
                # Update max_sum1 and max_idx_1 if sum1 is greater than max_sum1
                if sum1 > max_sum1:
                    max_sum1 = sum1
                    max_idx_1 = i - k * 3 + 1
              
                # Update max_sum1_2 and max_idx_1_2 if the combination of sum1 and sum2
                # provides a bigger sum than current max_sum1_2
                if max_sum1 + sum2 > max_sum1_2:
                    max_sum1_2 = max_sum1 + sum2
                    max_idx_1_2 = (max_idx_1, i - k * 2 + 1)
              
                # Update the res if the combination of sum1, sum2, and sum3 
                # is greater than the overall max sum found so far
                if max_sum1_2 + sum3 > sum:
                    sum = max_sum1_2 + sum3
                    res = [*max_idx_1_2, i - k + 1]
              
                # Slide the window for each subarray by subtracting the element that's no longer in the window
                sum1 -= nums[i - k * 3 + 1]
                sum2 -= nums[i - k * 2 + 1]
                sum3 -= nums[i - k + 1]
      
        # Return the indices of the first elements of the three subarrays
        return res



        ## S2: Ad-Hoc
        ## T: O(N)
        ## S: O(N)

        W = [] #array of sums of windows
        curr_sum = 0
        for i, x in enumerate(nums):
            curr_sum += x
            if i >= k: 
                curr_sum -= nums[i - k]
            if i >= k - 1: 
                W.append(curr_sum)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in range(k, len(W) - k):
            i, l = left[j - k], right[j + k]
            if ans is None or (W[i] + W[j] + W[l] > W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, l
        return ans

