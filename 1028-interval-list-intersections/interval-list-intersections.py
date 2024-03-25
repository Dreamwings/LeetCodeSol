class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        ## S1: Two Pointers
        ## T: O(M + N)
        ## S: O(K), K is num of intersections
        
        m, n = len(A), len(B)
        if m == 0 or n == 0: return []
        res = []
        i = j = 0
        
        while i < m and j < n:
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                res.append([lo, hi])
            if hi == A[i][1]:
                i += 1
            else:
                j += 1
        
        return res
        