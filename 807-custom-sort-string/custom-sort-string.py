class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        ## S1:
        ## T: O(N + M)
        ## T: O(N)

        d = collections.Counter(s)
        tmp = []

        for c in order:
            if c in d:
                tmp.append(c * d[c])
                del d[c]
        
        for k, v in d.items():
            tmp.append(k * v)

        return ''.join(tmp)

        """
        ## S1: Not good way of S1
        d = collections.Counter(s)
        res = '' # Using str concat will make time complexity very large
        # Creating a new str of len M comsumes time O(M)
        
        for c in order:
            if c in d:
                res += c * d[c]
                del d[c]
        
        for k, v in d.items():
            res += k * v
        
        return res
        """