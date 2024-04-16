class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        ## S2: DFS + Memory
        ## T: O(N^2) because at each char, the branching factor is 2, and no duplicated computing due to cache
        ## S: O(N^2)

        # Simple lightweight unbounded function cache, the same as lru_cache(maxsize=None)
        @cache 
        def isValid(i, j, kk):
            # check if s[i:j+1] is valid by removing at most kk chars
            if kk < 0:
                return False
            if i >= j:
                return True
                
            if s[i] == s[j]:
                return isValid(i + 1, j - 1, kk)
            else:
                return isValid(i + 1, j, kk - 1) or isValid(i, j - 1, kk - 1)

        return isValid(0, len(s) - 1, k)



        ## S3: DP
        ## T: O(N^2)
        ## S: O(N^2)

        n = len(s)
        dp = [[0] * n for _ in range(n)]
      
        # Each single character is a palindrome, so we fill the diagonal with 1's
        for i in range(n):
            dp[i][i] = 1
      
        for i in range(n - 2, -1, -1):
            # Start from the next character till the end of the string
            for j in range(i + 1, n):
                # If characters match, extend the n of the palindrome by 2
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                # If no match, take the maximum n of the palindrome without one of the characters
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
              
                # Check if the current palindromic subsequence plus allowed deletions covers the entire string
                if dp[i][j] + k >= n:
                    return True
      
        return False

        
        
        ## S1: Two Pointers + BFS
        ## T: O(N^2)
        ## S: O(N^2)

        # queue holds a tuple of `l` and `r`, and the depth `curr_k`.
        queue = deque([(0, len(s) - 1, 0)])
        visited = [[False for j in range(len(s))] for i in range(len(s))]
    
        while queue:
            l, r, curr_k = queue.popleft()

            # If the budget is exceeded return False
            if curr_k > k:
                return False

            # Shave off the two ends of s[l:r+1] until end characters 
            # don't match. Each graph node is defined by (l,r)
            # where s[l] != s[r].
            while s[l] == s[r]:
                l += 1
                r -= 1
                # if you reach the end node, you've found a k-palindrome
                if l >= r:
                    return True

            # append the two new nodes to the queue.
            if not visited[l+1][r]:
                queue.append((l+1, r, curr_k+1))
                visited[l+1][r] = True

            if not visited[l][r-1]:
                queue.append((l, r-1, curr_k+1))
                visited[l][r-1] = True


