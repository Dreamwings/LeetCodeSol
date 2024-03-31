class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ## S1: Binary Search
        ## T: O(log(MN))
        ## S: O(1)
        
        r, c = len(matrix), len(matrix[0])
        lo, hi = 0, r * c - 1
        
        while lo <= hi:
            m = (lo + hi) // 2
            x, y = m // c, m % c
            
            if target == matrix[x][y]:
                return True
            elif target > matrix[x][y]:
                lo = m + 1
            else:
                hi = m - 1
        
        return False
        
        