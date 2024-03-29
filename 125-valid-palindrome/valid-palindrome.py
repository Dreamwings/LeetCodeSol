class Solution:
    def isPalindrome(self, s: str) -> bool:

        ## S1: two pointers
        ## T: O(N)
        ## S: O(1)
        
        n = len(s)
        s = s.lower()
        if n <= 1: return True
        d = '0123456789abcdefghijklmnopqrstuvwxyz'
        i, j = 0, n - 1
        
        while i < j:
            while i < j and s[i] not in d:
                i += 1
            while i < j and s[j] not in d:
                j -= 1
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
                
        return True
        
        
        """
        ## S2:
        
        s = s.lower()
        q = []
        
        for x in s:
            if '0' <= x <= '9' or 'a' <= x <= 'z':
                q.append(x)
        
        return q == q[::-1]
        
        """
        
