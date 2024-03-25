class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        ## S2:
        ## T: O(MN)
        ## S: O(1)
        
        m, n = len(matrix), len(matrix[0])

        return all(matrix[i][j] == matrix[i+1][j+1] for i in range(m-1) for j in range(n-1))
        
        """
        ## S1:

        m, n = len(matrix), len(matrix[0])
        
        for i in range(m-1):
            for j in range(n-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
        """
        
                