class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        from collections import defaultdict

        ## S1: DFS
        
        n = len(grid)
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(x, y, idx):
            area = 1
            grid[x][y] = idx
            
            for dx, dy in dir:
                i, j = x + dx, y + dy
                if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                    area += dfs(i, j, idx)
            return area
        
        idx = 2
        d = defaultdict(int) # store the area of each island/idx
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j, idx)
                    d[idx] = area
                    idx += 1
                    
        if len(d) == 0: return 1
        res = max(d.values())
        
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    seen = set()
                    for dx, dy in dir:
                        i, j = x + dx, y + dy
                        if 0 <= i < n and 0 <= j < n and grid[i][j] > 1:
                            seen.add(grid[i][j])
                    
                    cur_area = 1  # change 0 cell (x, y) into 1
                    for idx in seen:
                        cur_area += d[idx]
                    res = max(res, cur_area)
        
        return res
                        
        ## S2: Union Find
        ## https://algo.monster/liteproblems/827