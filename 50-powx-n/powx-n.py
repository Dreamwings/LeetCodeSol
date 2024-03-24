class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        ## S1:
        if n == 0: return 1
        if x == 0:
            if n > 0: return 0
            if n < 0: raise ZeroDivisionError
        
        if n < 0: 
            x = 1/x
            n = -n
        
        p = 1
        while n:
            if n & 1:  # n odd
                p *= x
            n //= 2
            x = x * x
            
        return p
        """   
        ## S2

        def quick_power(base: float, exponent: int) -> float:
            result = 1.0
            # Continue multiplying the base until the exponent is zero
            while exponent:
                # If exponent is odd, multiply the result by the base
                if exponent & 1:
                    result *= base
                # Square the base (equivalent to base = pow(base, 2))
                base *= base
                # Right shift exponent by 1 (equivalent to dividing by 2)
                exponent >>= 1
            return result

        # If n is non-negative, call quick_power with x and n directly.
        # Otherwise, calculate the reciprocal of the positive power.
        return quick_power(x, n) if n >= 0 else 1 / quick_power(x, -n)
                