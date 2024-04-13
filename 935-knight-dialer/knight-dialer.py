class Solution:
    def knightDialer(self, n: int) -> int:
        
        ## S3: State Matrix 
        ## Time: O(logN)
        ## Space: O(1)
        
        import numpy as np
        K = 10**9 + 7
        ## M[i][j] stands for number of ways starting from i and ending at j with
        ## a single step
        ## Let M_k stands for M^k (the product of k M's)
        ## M_k[i][j] stands for number of ways starting from i and ending at j with
        ## (k - 1) steps
        M = np.matrix([[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                       [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]])
        
        x = np.matrix([1] * 10)
        n = n - 1
        
        while n:
            if n & 1:
                x = (x * M) % K
                n -= 1
            M = (M * M) % K
            n >>= 1
            
        return np.sum(x) % K
    
        """

        ## S2: Efficient Iteration On States
        ## See LeetCode Editorial
        ## Time: O(N)
        ## Space: O(1)

        # 1. If n = 1, return 10.
        # 2. Initialize A = 4, B = 2, C = 2, D = 1.
        # 3. Iterate n - 1 times:
        #     Perform the following updates simultaneously:
        #     A = 2 * (B + C)
        #     B = A
        #     C = A + 2 * D
        #     D = C
        # 4. Return A + B + C + D.
        
        if n == 1:
            return 10
        
        A = 4
        B = 2
        C = 2
        D = 1
        MOD = 10 ** 9 + 7
        
        for _ in range(n - 1):
            A, B, C, D = (2 * (B + C)) % MOD, A, (A + 2 * D) % MOD, C 
        
        return (A + B + C + D) % MOD

        

        ## S1:
        ## Time: O(N)
        ## Space: O(1)
        
        x = [1] * 10
        # x[i] means current total count when knight is at i, i is 0, 1, ..., 9
        K = 10**9 + 7
        
        for i in range(n-1): # jump n-1 steps
            y = [x[4] + x[6],  # you can jump from 4 or 6 to 0, so the total for next 0 state will be the sum of current 4 and 6
                 x[6] + x[8],
                 x[7] + x[9],
                 x[4] + x[8],
                 x[0] + x[3] + x[9],
                 0,
                 x[0] + x[1] + x[7],
                 x[2] + x[6],
                 x[1] + x[3],
                 x[2] + x[4]
                ]
            x = y
        
        return sum(x) % K
        """
        # d = {0: [4, 6],
        #      1: [6, 8],
        #      2: [7, 9],
        #      3: [4, 8],
        #      4: [0, 3, 9],
        #      5: [],
        #      6: [0, 1, 7],
        #      7: [2, 6],
        #      8: [1, 3],
        #      9: [2, 4]}
        
        