class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        ## Solution 1: DFS
        ## T: O(M * N)
        ## S: O(M * N)
        
        m, n = len(grid), len(grid[0])
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(x, y):
            grid[x][y] = '0'
            
            for dx, dy in dir:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                    dfs(i, j)
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
                    
        return res
        
        """
        ## Solution 2: BFS
        ## T: O(M * N)
        ## S: O(M * N)
        
        from collections import deque
        
        def bfs(x, y):
            q = deque()
            q.append((x, y))
            grid[x][y] = '0'
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            while q:
                X, Y = q.popleft()
                for dx, dy in d:
                    i, j = X + dx, Y + dy
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                        q.append((i, j))
                        grid[i][j] = '0'
                        
            return
                    
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i, j)
                    res += 1
        
        return res
        
        
        """
        
