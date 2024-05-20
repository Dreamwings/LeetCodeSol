class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        ## S1: Hash Table
        ## T: O(N)
        ## S: O(N)

        r = sum(nums) % p
        # If the sum of nums is already divisible by p, the subarray length is 0
        if r == 0:
            return 0

        # Hash map to store the most recent index where a particular mod value is found
        d = {0: -1}
        cur_mod = 0 # The current prefix sum mod p
        min_len = len(nums) # Initialize minimum length to the length of nums array

        for i, x in enumerate(nums):
            # Update the current mod value
            cur_mod = (cur_mod + x) % p
            # Calculate the target mod value which would balance 
            # the current mod to make a divisible sum
            t = (cur_mod - r + p) % p

            # If the target mod value is found in the d
            if t in d:
                # Update the min_len if a shorter subarray is found
                min_len = min(min_len, i - d[t])
            # Update the d with the current i
            d[cur_mod] = i

        return -1 if min_len == len(nums) else min_len