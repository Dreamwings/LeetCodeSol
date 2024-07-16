class Solution:
    def countGoodNumbers(self, n: int) -> int:

        ## S1: 
        ## T: O(logN)
        ## S: O(1)
        
        M = 10**9 + 7 
      
        # Define the power function to calculate (x^n) % M using binary exponentiation.
        def my_pow(base, exp):
            result = 1
            while exp > 0:
                # If exp is odd, multiply the result with base.
                if exp % 2 == 1:
                    result = (result * base) % M
                # Square the base and reduce the exp by half.
                base = (base * base) % M
                exp //= 2
            return result
      
        # Number of primes at odd positions is 5 (2,3,5,7). Hence, we use 5 as the base.
        # Number of evens at even positions is 4 (0,2,4,6,8). Hence, we use 4 as the base. Even positions are considered 0-indexed here.
        # The +1 is needed when n is odd, to calculate 5 raised to the (n//2 + 1).
        return (my_pow(5, (n + 1) // 2) * my_pow(4, n // 2)) % M