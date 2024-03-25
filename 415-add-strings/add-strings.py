class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        ## S1: Two Pointers
        ## T: O(max(M, N))
        ## S: O(max(M, N))
        
        i, j, s, c = len(num1) - 1, len(num2) - 1, 0, 0
        res = ''
        
        while i >= 0 or j >= 0 or c:
            s += c
            if i >= 0:
                s += int(num1[i])
                i -= 1
            if j >= 0:
                s += int(num2[j])
                j -= 1
            
            c = s // 10
            res += str(s % 10)
            s = 0
        
        return res[::-1]