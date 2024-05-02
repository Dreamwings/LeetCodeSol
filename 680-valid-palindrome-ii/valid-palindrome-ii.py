class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        ## S3: Two Pointers
        ## Time: O(N)
        ## Space: O(1)

        def is_valid(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        i, j = 0, len(s) - 1 

        while i < j:
            if s[i] != s[j]:
                return is_valid(i, j - 1) or is_valid(i + 1, j)
            
            i, j = i + 1, j - 1

        return True


        
        ## S1: Two Pointers
        ## Time: O(N)
        ## Space: O(N)
        
        n = len(s)
        if n == 1: return True
        l, r = 0, n - 1
        
        while l < r:
            if s[l] != s[r]:
                x = s[l : r]
                y = s[l+1 : r+1]
                return x == x[::-1] or y == y[::-1]
            l += 1
            r -= 1
        return True
        
        

        ## S2:
        
        def helper(l, r):
            if l >= r: return True
            
            if s[l] != s[r]:
                x = s[l : r]
                y = s[l+1 : r+1]
                return x == x[::-1] or y == y[::-1]
            else:
                return helper(l+1, r-1)
        
        return helper(0, len(s)-1)    

        