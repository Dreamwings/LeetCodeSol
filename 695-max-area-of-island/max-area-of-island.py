class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ## S1: DFS
        ## T: O(M*N)
        ## S: O(M*N)

        m, n = len(grid), len(grid[0])
        
        def dfs(x, y):
            area = 1
            grid[x][y] = 0
            
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in d:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and grid[i][j]:
                    area += dfs(i, j)
            return area
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    area = dfs(i, j)
                    res = max(res, area)
                
        return res
