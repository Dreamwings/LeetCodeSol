class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        ## S1: Counter
        ## T: O(N), N = len(s)
        ## T: O(N)

        d = collections.Counter(s)
        arr = []  # Array to hold ordered substrings for each ch

        for c in order:
            if c in d:
                arr.append(c * d[c])
                del d[c]
                # d[c] = 0 # Also works.
        
        for k, v in d.items():
            arr.append(k * v)

        return ''.join(arr)



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
        