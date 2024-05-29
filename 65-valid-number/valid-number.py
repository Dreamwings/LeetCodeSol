class Solution:
    def isNumber(self, s: str) -> bool:

        ## S2:
        ## T: O(N)
        ## S: O(N)
        # special = {"inf", "-inf", "+inf", "Infinity", "infinity", "+Infinity", 
        #            "-Infinity", "+infinity", "-infinity", "nan"}

        try:
            if "inf" in s.lower() or "nan" in s.lower():  # check for special float values
                return False
            num = float(s)
            return True
        except ValueError:
            return False



        ## S1:
        ## T: O(N)
        ## S: O(1)

        # s = s.strip()
        if not s:
            return False

        seen_dig = seen_e = seen_dot = False

        for i, c in enumerate(s):
            if c.isdigit():
                seen_dig = True
            elif c in ["+", "-"]:
                if i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
            elif c in ["e", "E"]:
                if seen_e or not seen_dig:
                    return False
                seen_e = True
                seen_dig = False
            elif c == ".":
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            else:
                return False

        return seen_dig
        


        ## S3: Regular Expression by ChatGPT
        ## T: O(N)
        ## S: O(N)

        import re

        pattern = re.compile(r'''
            ^                   # start of string
            [+-]?               # optional sign
            (                   # start of main number part
                (\d+(\.\d*)?)   # digits followed by an optional decimal point and optional digits
                |               # OR
                (\.\d+)         # a decimal point followed by digits
            )                   # end of main number part
            ([eE][+-]?\d+)?     # optional exponent part with 'e' or 'E' followed by an optional sign and digits
            $                   # end of string
        ''', re.VERBOSE)
        
        return bool(pattern.match(s))
        
