class Solution:
    def frequencySort(self, s: str) -> str:
        
        from collections import Counter
        
        ## S1:
        
        d = Counter(s).most_common()
        
        res = ''.join(c * n for c, n in d)
        
        return res

        """
        ## Solution 2:
        
        d = Counter(s)
        
        arr = sorted(d, key=lambda x: -d[x])
        res = ''
        
        for c in arr:
            res += c * d[c]
        
        return res
        """
        
