class Solution:
    def findRLEArray(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        
        ## S1: Two Pointers
        ## T: O(N + M)
        ## S: O(1)

        m, n = len(a), len(b)
        i = j = 0
        res = []
        while i < m and j < n:
            p = a[i][0] * b[j][0]
            if a[i][1] == b[j][1]:
                res.append([p, a[i][1]])
                i += 1
                j += 1
            elif a[i][1] > b[j][1]:
                res.append([p, b[j][1]])
                a[i][1] -= b[j][1]
                j += 1
            else:
                res.append([p, a[i][1]])
                b[j][1] -= a[i][1]
                i += 1
            if len(res) > 1 and res[-1][0] == res[-2][0]:
                res[-2][1] += res[-1][1]
                res.pop()
        return res

        