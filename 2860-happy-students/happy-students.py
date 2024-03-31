class Solution:
    def countWays(self, nums: List[int]) -> int:
        
        ## S1: Sort

        nums.sort()
        n = len(nums)
        answer = 0
      
        # Iterate over all elements in the sorted list
        for i in range(n + 1):
            # If not the first element, and the previous number is greater than or equal to the index, skip
            if i > 0 and nums[i - 1] >= i:
                continue
          
            # If not the last element, and the current number is less than or equal to the index, skip
            if i < n and nums[i] <= i:
                continue

            answer += 1
      
        # At this point the answer is not changed by the loop, this loop has no effect. 
        # The function currently will always return 0 as it stands.
        return answer