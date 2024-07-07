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
        


        ## S2: DFS with Cache

        combos = []
        # 1. find all possible bottom row combination (combos)
        def get_combos(cur, cur_sum):                     
            nonlocal combos, width
            if cur_sum > width: return
            if cur_sum == width:
                combos.append(tuple(cur)) 
                return
            for brick in bricks:
                get_combos(cur + [brick], cur_sum + brick)
        get_combos([], 0)
        
        d = collections.defaultdict(list) # make a adjacency list for {combo: [possible_neighbor_row...]}
        
        # 2. for each `combo`, find its possible neighbor row
        for i, combo in enumerate(combos):                
            s, cur = set(), 0
            for val in combo[:-1]:                        
                s.add(cur:=cur+val)
            for j, nei in enumerate(combos):    
                cur = 0                
                for val in nei[:-1]:
                    cur += val
                    if cur in s: break
                else:                        
                    d[combo].append(nei)
                    
        ans, mod = 0, int(1e9+7)
        
        # count number of ways build brick up to `height` 
        @cache
        def dfs(combo, h):                                
            nonlocal ans, d, height
            if height == h: return 1
            return sum(dfs(nei, h+1) for nei in d[combo])

        # 3. for each `combo`, starting from bottom row, build up to `height`    
        for combo in combos:                              
            ans += dfs(combo, 1) % mod
            
        return ans % mod   

