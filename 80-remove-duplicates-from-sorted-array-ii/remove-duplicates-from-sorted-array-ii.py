class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        ## S1:

        unique_count = 0
      
        for num in nums:
            # Check if the current number is different from the number
            # at position unique_count - 2.
            # This is to allow a maximum of two duplicates.
            if unique_count < 2 or num != nums[unique_count - 2]:
                # If condition met, copy the current number to the next position in the array.
                nums[unique_count] = num
                # Increment the count of unique elements.
                unique_count += 1
              
        return unique_count
