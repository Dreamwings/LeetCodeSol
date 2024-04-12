class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        ## S1: DFS + Memorization (DP)
        ## T: O(N^2)
        ## S: O(N^2)

        n = len(cost)
      
        # Define the memoization decorator to cache results of the recursive function
        @lru_cache(None)
        def dfs(wall_index: int, time_remaining: int) -> int:
            # Base case 1: If there are fewer walls left than the current time,
            # the cost is 0 as no more painting is needed.
            if n - wall_index <= time_remaining:
                return 0
          
            # Base case 2: If all walls are considered, return infinity because
            # exceeding time is not permissible.
            if wall_index >= n:
                return float('inf')
          
            # Recursively consider two options and take the minimum:
            # 1. Paint the current wall (increment time and add the cost)
            # 2. Skip the current wall (decrement the time but no cost)
            return min(
                dfs(wall_index + 1, time_remaining + time[wall_index]) + cost[wall_index],
                dfs(wall_index + 1, time_remaining - 1)
            )
      
        return dfs(0, 0)

        """

        ## S2: DP Bottom-Up 
        ## T: O(N^2)
        ## S: O(N^2)

        n = len(cost)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            dp[n][i] = inf

        for i in range(n - 1, -1, -1):
            for remain in range(1, n + 1):
                paint = cost[i] + dp[i + 1][max(0, remain - 1 - time[i])]
                dont_paint = dp[i + 1][remain]
                dp[i][remain] = min(paint, dont_paint)
        
        return dp[0][n]

        ## S3: DP Top-Down 
        ## T: O(N^2)
        ## S: O(N^2)

        @cache
        def dp(i, remain):
            if remain <= 0:
                return 0
            if i == n:
                return inf
            
            paint = cost[i] + dp(i + 1, remain - 1 - time[i])
            dont_paint = dp(i + 1, remain)
            return min(paint, dont_paint)
    
        n = len(cost)
        return dp(0, n)

        """
