class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        if S == '': 
            return 0
        missing_l, missing_r = 0, 0
        
        for c in S:
            if c == '(':
                missing_r += 1
            elif missing_r > 0:
                missing_r -= 1
            else:
                missing_l += 1
        
        return missing_l + missing_r