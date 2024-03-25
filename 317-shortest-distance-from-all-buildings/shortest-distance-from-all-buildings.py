class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        from collections import defaultdict

        ## S1 BFS

        if not grid or not grid[0]: return -1
        m, n = len(grid), len(grid[0])
        dd = defaultdict(int)  # store the dist sum at each 0 cell to the 1 cells (buildings)
        num_ones = defaultdict(int)  # store how many buildings visited 0 cell (x, y)
        
        def valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 0

        def bfs(x, y):
            seen = set()
            dist = 0
            q = [(x, y)]
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            while q:
                nxt = []
                dist += 1
                for xx, yy in q:
                    for dx, dy in d:
                        i, j = xx + dx, yy + dy
                        if valid(i, j) and (i, j) not in seen:
                            seen.add((i, j))
                            nxt.append((i, j))
                            dd[(i, j)] += dist
                            num_ones[(i, j)] += 1  # IMPORTANT!!!
                            
                q = nxt
        
        tot_ones = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    tot_ones += 1
                    bfs(i, j)
        
        min_dist = float('inf')
        for (x, y) in dd:
            if num_ones[(x, y)] == tot_ones:  # IMPORTANT!!!
                min_dist = min(min_dist, dd[(x, y)])

        return -1 if min_dist == float('inf') else min_dist


