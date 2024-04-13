class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        ## S1: Brian Kernighan's Algorithm
        ## T: O(1), Although there is a loop in the algorithm, the number of iterations is bounded 
        ##          by the number of bits that an integer has, which is fixed: log2(max_int) bits
        ## S: O(1)

        # Loop until 'left' is not less than 'right'
        while left < right:
            # We use the trick "right &= right - 1" to clear the least significant bit of 'right'
            # This effectively reduces 'right' each time, moving towards 'left'
            right &= right - 1
      
        # At the point where the while loop stops, 'left' and 'right' have the same prefix for 
        # their binary representations which is the answer to the problem.
        return right

        """

        ## S2: Bit Shift
        ## T: O(1), Although there is a loop in the algorithm, the number of iterations is bounded 
        ##          by the number of bits that an integer has, which is fixed: log2(max_int) bits
        ## S: O(1)

        shift = 0   

        # find the common 1-bits
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift

        """