class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        ## S2: DFS + Memory
        ## T: O(M*N)
        ## S: O(M*N)

        m, n = len(matrix), len(matrix[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
      
        # Use memoization to cache the results of previous computations
        @lru_cache(maxsize=None)
        def dfs(x: int, y: int) -> int:
            # Start with the longest path of 1 that includes the current cell
            max_path_length = 1
          
            # Explore all possible directions from the current cell
            for dx, dy in directions:
                i, j = x + dx, y + dy
              
                # Check if the new position is within bounds and increases in value
                if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[x][y]:
                    # Recursively find the longest increasing path from the new position
                    max_path_length = max(max_path_length, 1 + dfs(i, j))
                  
            return max_path_length

        # Iterate over all matrix cells to find the starting point of the longest increasing path
        max_path = 0
        for i in range(m):
            for j in range(n):
                max_path = max(max_path, dfs(i, j))
              
        return max_path

        """

        ## S1: DFS

        m, n = len(matrix), len(matrix[0])
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        g = [[0] * n for _ in range(m)]
        
        def dfs(x, y):
            if not g[x][y]: # (x, y) is not visited yet
                cur_max = 0
                for dx, dy in dir:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[x][y]:
                        cur_max = max(cur_max, dfs(i, j))
                g[x][y] = 1 + cur_max
            
            return g[x][y]
                
        res = 0
        for i in range(m):
            for j in range(n):
                g[i][j] = dfs(i, j)
                res = max(res, g[i][j])
        return res
        """