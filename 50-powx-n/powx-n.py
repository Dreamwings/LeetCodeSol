class Solution:
    def myPow(self, x: float, n: int) -> float:

        ## S2
        ## T: O(logN)
        ## S: O(1)

        def quick_power(base, exp):
            res = 1.0
            # Continue multiplying the base until the exponent is zero
            while exp:
                # If exponent is odd, multiply the res by the base
                if exp & 1:
                    res *= base
                # Square the base (equivalent to base = pow(base, 2))
                base *= base
                # Right shift exponent by 1 (equivalent to dividing by 2)
                exp >>= 1
            return res

        if n >= 0: 
            return quick_power(x, n) 
        else:
            return 1 / quick_power(x, -n)
            # return quick_power(1/x, -n) 

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
        