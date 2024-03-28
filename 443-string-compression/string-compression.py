class Solution:
    def compress(self, chars: List[str]) -> int:
        
        ## S1: Two Pointers
        ## T: O(N)
        ## S: O(1)
        
        n = len(chars)
        p = i = 0
        
        while i < n:
            ch, cnt = chars[i], 1
            chars[p] = ch
            p += 1
            
            while i + 1 < n and chars[i+1] == ch:
                cnt += 1
                i += 1
            
            if cnt > 1:
                for x in str(cnt):
                    chars[p] = x
                    p += 1
            
            i += 1
        
        return p
            