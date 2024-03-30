class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        
        ## S1: Two Pointers

        m, n = len(encoded1), len(encoded2)
        i = j = 0
        res = []
        while i < m and j < n:
            val = encoded1[i][0] * encoded2[j][0]
            if encoded1[i][1] == encoded2[j][1]:
                res.append([val, encoded1[i][1]])
                i += 1
                j += 1
            elif encoded1[i][1] > encoded2[j][1]:
                res.append([val, encoded2[j][1]])
                encoded1[i][1] -= encoded2[j][1]
                j += 1
            else:
                res.append([val, encoded1[i][1]])
                encoded2[j][1] -= encoded1[i][1]
                i += 1
            if len(res) > 1 and res[-1][0] == res[-2][0]:
                res[-2][1] += res[-1][1]
                res.pop()
        return res
        