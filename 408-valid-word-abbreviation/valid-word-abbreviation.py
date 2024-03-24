class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        ## S2: Two Pointers (No nested Loop)
        ## T: O(M+N)
        ## S: O(1)

        i, j, m, prev = len(word), len(abbr), 1, None
        
        while i > 0 and j > 0:
            c1, c2 = word[i-1], abbr[j-1]
            if c1 == c2:
                i -= 1
                j -= 1
                m = 1
                if prev == 0: 
                    return False
            elif c2.isdigit():
                i -= int(c2) * m
                j -= 1
                m *= 10
                prev = int(c2)
            else: 
                return False
        
        return i == j == 0

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
        
