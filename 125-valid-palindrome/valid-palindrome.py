class Solution:
    def isPalindrome(self, s: str) -> bool:

        ## S3: two pointers
        ## T: O(N)
        ## S: O(1)

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

        

        ## S2: two pointers
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
        
        

        ## S1:
        ## T: O(N)
        ## S: O(N)

        s = s.lower()
        q = []
        
        for x in s:
            if '0' <= x <= '9' or 'a' <= x <= 'z':
                q.append(x)
        
        return q == q[::-1]
        

        
