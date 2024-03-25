class Solution:
    def isNumber(self, s: str) -> bool:
        
        ## S1:
        ## T: O(1)
        ## S: O(N)
        # special = {"inf", "-inf", "+inf", "Infinity", "infinity", "+Infinity", "-Infinity", "+infinity", "-infinity", "nan"}

        try:
            if "inf" in s or "Inf" in s or "nan" in s: # s in special
                return False
            num = float(s)
            return True
        except:
            return False

        """
        ## S2:
        ## T: O(N)
        ## S: O(1)

        s = s.strip()
        if not s:
            return False

        seenNum = False
        seenDot = False
        seenE = False

        for i, c in enumerate(s):
            if c == '.':
                if seenDot or seenE:
                    return False
                seenDot = True
            elif c == 'e' or c == 'E':
                if seenE or not seenNum:
                    return False
                seenE = True
                seenNum = False
            elif c in '+-':
                if i > 0 and s[i - 1] not in 'eE':
                    return False
                seenNum = False
            else:
                if not c.isdigit():
                    return False
                seenNum = True

        return seenNum
        """
        