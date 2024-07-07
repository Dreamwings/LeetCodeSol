class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        from collections import defaultdict
        
        ## S1: DFS + DP
        ## B = len(bricks), K is the max num of bricks a row can take
        ## H = height, W = width, N = len(all_rows) ~ B**K
        ## T: O(B**K + N**2 * W + N**2 + H * N**2) ~ O(H * N**2) = O(H * B**(2K))
        ## S: ~ O(H * N**2) = O(H * B**(2K))

        M = 10 ** 9 + 7
        all_rows, cur_row = [], [] # To store all possible configurations and the one for current row

        # Helper function to find all possible ways to build a single layer
        # O(B**K), B = len(bricks), K is the max num of bricks a row can take
        def dfs(idx): 
            # idx: the idx of current row
            if idx > width:
                return
            if idx == width:
                all_rows.append(cur_row[:])
                return
            
            for w_brick in bricks:
                cur_row.append(w_brick)
                dfs(idx + w_brick)
                cur_row.pop()

        # Function to check if two configurations can be placed one over the other
        # O(N**2 * W), N = len(all_rows), W = width
        def is_compatible(row1, row2):
            sum1, sum2 = row1[0], row2[0] # Current total width of the two rows
            i, j = 1, 1 # Two pointers

            while i < len(row1) and j < len(row2): # Rows might have different lengths
                if sum1 == sum2:
                    return False
                if sum1 < sum2:
                    sum1 += row1[i]
                    i += 1
                else:
                    sum2 += row2[j]
                    j += 1
            
            return True
        
        # Create all possible rows starting from row 0
        dfs(0)

        graph = defaultdict(list) # To store the compatible rows which can be adjacent
        tot_rows = len(all_rows)
        
        # Build the graph
        # O(N**2)
        for i in range(tot_rows):
            # One special case: brick_width = width, when you just need to use one brick for the row,
            # it always compatible with itself. Need to add this to the compatible graph
            # Example: height = 2, width = 6, bricks = [1, 2, 6]
            if is_compatible(all_rows[i], all_rows[i]):
                    graph[i].append(i)
            for j in range(i + 1, tot_rows):
                if is_compatible(all_rows[i], all_rows[j]):
                    graph[i].append(j)
                    graph[j].append(i)
        
        dp = [[0] * tot_rows for _ in range(height)]

        for j in range(tot_rows):
            dp[0][j] = 1 # Each configuration is one way to build the first layer
        
        # Compute number of ways to build the wall using DP
        # O(H * N**2)
        for i in range(1, height):
            for j in range(tot_rows):
                for k in graph[j]:
                    dp[i][j] += dp[i-1][k]
                    dp[i][j] %= M
        
        return sum(dp[-1]) % M
        