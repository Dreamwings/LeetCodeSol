class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        from collections import defaultdict
        
        ## S1: Two for loops
        ## T: O(MN + (M+N)log(M+N))
        ## S: O(M+N)
        
        m, n = len(mat), len(mat[0])
        d = defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                d[i + j].append(mat[i][j]) 
        
        res = []
        for k in sorted(d):
            if k & 1:
                res += d[k]
            else:
                res += d[k][::-1]
        
        return res
        
        """

        ## S2: One for loop + One while loop
        ## T: O((M+N)*N)
        ## S: O(M+N)
        m, n = len(matrix), len(matrix[0])
      
        # This is the list which will hold the elements in diagonal order.
        res = []
      
        # There will be (m + n - 1) diagonals to cover in the matrix.
        for k in range(m + n - 1):
          
            # Temp list to store the elements of the current diagonal.
            temp = []
          
            # Calculate the starting row index. It is 0 for the first 'n' diagonals,
            # otherwise we start at an index which goes down from 'm - 1'.
            row = 0 if k < n else k - n + 1
          
            # Calculate the starting column index. It is 'k' for the first 'n' diagonals,
            # otherwise we start at 'n - 1' and go down.
            col = k if k < n else n - 1
          
            # Fetch the elements along the current diagonal.
            # Continue while 'row' is within the matrix row range and 'col' is non-negative.
            while row < m and col >= 0:
                temp.append(matrix[row][col])
                row += 1  # Move down to the next row.
                col -= 1  # Move left to the next column.
          
            # Reverse every other diagonal's elements before appending it to the result list
            # to get the right order.
            if k % 2 == 0:
                temp = temp[::-1]
          
            # Extend the main result list with the elements of the current diagonal.
            res.extend(temp)
      
        # Return the final result list.
        return res

        ## S3
        
        m, n = len(mat), len(mat[0])
        res = []
        f = 0
        i, j = 0, 0
        
        while len(res) < m * n:
            res.append(mat[i][j])
            if f == 0:
                if j == n - 1:
                    f = 1
                    i += 1
                elif i == 0:
                    f = 1
                    j += 1
                else:
                    i, j = i - 1, j + 1
            else:
                if i == m - 1:
                    f = 0
                    j += 1
                elif j == 0:
                    f = 0
                    i += 1
                else:
                    i, j = i + 1, j - 1
        
        return res            
        """
                