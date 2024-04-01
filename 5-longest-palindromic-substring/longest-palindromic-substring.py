class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        ## Solution 4: Manacher's Algorithm
        ## Time: O(N)
        S = '@#' + '#'.join(s) + '#$'
        n = len(S)
        Z = [0] * n
        C, R = 0, 0
        max_len, max_ctr = 0, 0
        
        for i in range(n-1):
            k = 2 * C - i
            if i < R:
                Z[i] = min(Z[k], R - i)
            
            while S[i + Z[i] + 1] == S[i - Z[i] - 1]:
                Z[i] += 1
            
            if i + Z[i] > R:
                C, R = i, i + Z[i]
            
            if Z[i] > max_len:
                max_len = Z[i]
                max_ctr = i
        
        lo = (max_ctr - max_len) >> 1
        hi = (max_ctr + max_len) >> 1
        return s[lo:hi]
        
        
        """
        ## Solution 2: Optimized O(N^2)
        ## https://leetcode.com/problems/longest-palindromic-substring/discuss/2925/Python-O(n2)-method-with-some-optimization-88ms.
        ## much faster due to Python tricks in comparing strings which is immutable.
        
        n = len(s)
        if n == 0 or n == 1: return s
        
        L = 1  # max length so far
        start = 0
        
        for j in range(1, n): # j is the ending index of substring
            i = j - L
            if i >= 1 and s[i-1 : j+1] == s[i-1 : j+1][::-1]:
                start = i - 1
                L += 2
                continue
            
            if i >= 0 and s[i : j+1] == s[i : j+1][::-1]:
                start = i
                L += 1
                
        return s[start : start + L]
        
        
        
        ## Solution 1:
        ## Time: O(N^2)
        ## Space: O(1)
        
        def palindrome(s, i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1 : j]
        
        res = ''
        for i in range(len(s)):
            odd = palindrome(s, i, i)
            even = palindrome(s, i, i+1)
            res = max(res, odd, even, key=len)
            
        return res
        
        
        ## Solution 3: DP (TLE)
        ## Time: O(N^2)
        ## Space: O(N^2)
        
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        max_len = 1
        start= 0
        
        for L in range(2, n+1):  # L is string length
            for i in range(n):   # i is string left index
                j = i + L - 1
                if j >= n:
                    break
                
                if s[i] != s[j]:
                    dp[i][j] = False
                elif j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
                
                if dp[i][j] == True and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start, end = i, j+1
                    
        
        return s[start : start + max_len]
        """