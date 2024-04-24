class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        ## S1: Sliding Window (Two Pointers)
        ## T: O(N)
        ## S: O(1)

        i = 0
        pre_zeros = 0
        s = 0 # current prefix sum
        res = 0
        
        # Loop through the array using j pointer
        for j, x in enumerate(nums):
            # Add current element to the sum
            s += x
            
            # Slide the window while condition is met
            while i < j and (nums[i] == 0 or s > goal):
                if nums[i] == 1:
                    pre_zeros = 0
                else:
                    pre_zeros += 1
                
                s -= nums[i]
                i += 1
                
            # Count subarrays when window sum matches the goal
            if s == goal:
                res += 1 + pre_zeros  
                
        return res
