class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        ## S1: Two Pointers
        ## Time: O(N)
        ## Space: O(1)
        
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
        """
        
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

        ## S3: Two Pointers
        ## Time: O(N)
        ## Space: O(1)

        def is_palindrome(left, right):
            while left < right:
                if string[left] != string[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        left, right = 0, len(string) - 1 

        while left < right:
            if string[left] != string[right]:
                return is_palindrome(left, right - 1) or is_palindrome(left + 1, right)
            
            left, right = left + 1, right - 1

        return True

        """
        
        