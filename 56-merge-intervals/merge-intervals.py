class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        
        ## S1: Sorting
        ## T: O(NlogN)
        ## S: O(N)
        if len(a) <= 1: return a
        a.sort(key=lambda x: x[0])
        res = [a[0]]

        for x in a[1:]:
            if x[0] <= res[-1][1]:
                res[-1][1] = max(x[1], res[-1][1])
            else:
                res.append(x)
        return res