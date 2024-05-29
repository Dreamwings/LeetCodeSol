class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        ## S1:
        ## T: O(D), D = denominator
        ## S: O(D)

        from collections import defaultdict
        
        if numerator == 0: return '0'
        if numerator % denominator == 0: return str(numerator // denominator)
        neg = (numerator < 0) ^ (denominator < 0)
        nu, de = abs(numerator), abs(denominator)
        
        sign = '-' if neg else ''
        q, m = nu // de, nu % de
        res = sign + str(q) + '.'
        dec = []
        rem = defaultdict(int)  # to store the location of each digit of decimal part
        
        while m:
            if m in rem:
                pos = rem[m]
                dec.insert(pos, '(')
                dec.append(')')
                break
            
            rem[m] = len(dec)
            m *= 10
            dec.append(str(m // de))
            m = m % de
            
        return res + ''.join(dec)