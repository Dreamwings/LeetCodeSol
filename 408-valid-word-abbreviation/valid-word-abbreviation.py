class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        ## S2: Two Pointers (No nested Loop, from right to left)
        ## T: O(N)
        ## S: O(1)

        i, j = len(word) - 1, len(abbr) - 1
        m, prev = 1, None # m is a multiplier, prev is to check if first digit is 0
        
        while i >= 0 and j >= 0:
            x, y = word[i], abbr[j]
            if x == y:
                i -= 1
                j -= 1
                m = 1
                if prev == 0: 
                    return False
            elif y.isdigit():
                i -= int(y) * m
                j -= 1
                m *= 10
                prev = int(y)
            else: 
                return False
        
        return i == j == -1


        """
        ## S1: Two Pointers
        ## T: O(M+N)
        ## S: O(1)
        m, n = len(word), len(abbr)
        i, j = 0, 0

        while i < m and j < n:
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                x = j
                while j < n and abbr[j].isdigit():
                    j += 1
                i += int(abbr[x : j])
            elif word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                return False
        
        if (i, j) == (m, n): return True
        return False        
        
        """