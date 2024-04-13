class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        ## S2: Math
        ## T: O(logK)
        ## S: O(1)

        # Calculate the bit count (number of set bits) of k-1.
        # In Python, the bit_count method of integers returns the number of 1's in the binary representation of the number.
        bit_count = bin(k - 1).count('1')

        # Determine the k-th element by checking if the bit count is odd
        # The '&' operator is a bitwise AND that results in 1 if the bit_count is odd (since 1 & 1 = 1),
        # and 0 if the bit_count is even (since even_number & 1 = 0).
        return bit_count & 1



        ## S1: Recursion
        ## T: O(N)
        ## S: O(N)

        def helper(n: int, k: int) -> int:
            # First row will only have one symbol '0'.
            if n == 1:
                return 0

            total_elements = 2 ** (n - 1)
            half_elements = total_elements // 2

            # If the target is present in the right half, we switch to the respective left half symbol.
            if k > half_elements:
                return 1 - helper(n, k - half_elements)

            # Otherwise, we switch to the previous row.
            return helper(n - 1, k)

        return helper(n, k)

        