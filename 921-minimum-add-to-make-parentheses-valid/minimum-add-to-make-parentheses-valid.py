class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """

        ## S1: 
        ## T: O(N)
        ## S: O(1)
        
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


        ## S2: 
        ## T: O(N)
        ## S: O(1)

        ans = bal = 0
        for symbol in S:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal