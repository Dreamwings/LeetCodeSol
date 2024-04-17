class Solution:
    def maximumSwap(self, num: int) -> int:
        
        from collections import defaultdict
        
        ## S1: Greedy
        ## T: O(N)
        ## S: O(N)

        a = list(map(int, str(num)))  # Note in Python 3, need to use list for map function
        # a = [int(x) for x in str(num)]
        last = defaultdict(int) # Must have a default value for each from "0123456789"
        for i, x in enumerate(a):
            last[x] = i
        
        for i, x in enumerate(a):
            for n in range(9, x, -1):
                if last[n] > i:
                    a[i], a[last[n]] = a[last[n]], a[i]
                    return int(''.join([str(x) for x in a]))
        
        return num



        ## S2:

        digits = list(str(num))
        n = len(digits)
        # Create a list to keep track of the indices of the digits
        # that should be considered for swapping.
        last = list(range(n))
      
        # Populate the last list with the index of the maximum digit
        for i in range(n - 2, -1, -1):
            # If the current digit is less than or equal to the maximum digit found
            # to its right, update the last for the current position.
            if digits[i] <= digits[last[i + 1]]:
                last[i] = last[i + 1]
      
        # Loop through each digit to find the first instance where a swap would
        # increase the value of the number. Swap and break the loop.
        for i in range(n):
            max_index = last[i]
            # If the current digit is smaller than the maximum digit to its right,
            # swap the two digits.
            if digits[i] < digits[max_index]:
                # Swap the current digit with the maximum digit found.
                digits[i], digits[max_index] = digits[max_index], digits[i]
                # Only one swap is needed, so break after swapping.
                break
      
        # Convert the list of digits back to a string and then to an integer.
        return int(''.join(digits))

