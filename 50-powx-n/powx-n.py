class Solution:
    def myPow(self, x: float, n: int) -> float:

        ## S5: Using **
        
        return x ** n
                
        ## S4: Using Math Lib

        return math.pow(x, n); 

                
        ## S1: Iterative
        ## T: O(logN)
        ## S: O(1)

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
 


        ## S3: Recursive
        ## T: O(logN)
        ## S: O(logN)

        # Base case, to stop recursive calls.
        if n == 0:
            return 1
        # Handle case for n < 0.
        if n < 0:
            return 1.0 / self.myPow(x, -1 * n)
       
        # Perform Binary Exponentiation.
        # If 'n' is odd, compute 'n - 1' case and multiply result with 'x'.
        if n % 2 == 1:
            return x * self.myPow(x * x, (n - 1) // 2)
        # Otherwise we calculate result by performing Binary Exponentiation on 'n'.
        else:
            return self.myPow(x * x, n // 2)


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
        