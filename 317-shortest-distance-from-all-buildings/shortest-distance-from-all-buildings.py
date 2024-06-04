class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        from collections import defaultdict
        
        ## S2: BFS with Pruning (Optimized from S1)
        ## From houses to empty land
        ## T: O((M*N)^2)
        ## S: O(MN)

        if not grid or not grid[0]: return -1
        m, n = len(grid), len(grid[0])
        dd = defaultdict(int)  # Stores the dist sum at each 0 cell to the 1 cells (buildings)
        num_ones = defaultdict(int)  # Stores how many buildings visited 0 cell (x, y)
        tot_ones = sum(v for row in grid for v in row if v == 1)
        
        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        def bfs(x, y):
            seen = set()
            seen.add((x, y))
            dist = 0
            seen_ones = 1 # How many "1"s seen by (x, y) including itself
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
                            if grid[i][j] == 0:
                                nxt.append((i, j))
                                dd[(i, j)] += dist
                                num_ones[(i, j)] += 1  # IMPORTANT!!!
                            elif grid[i][j] == 1:  # For pruning
                                seen_ones += 1
                q = nxt
            return seen_ones == tot_ones
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if not bfs(i, j): # For pruning, early exit
                        return -1
        
        min_dist = float('inf')
        for (x, y) in dd:
            if num_ones[(x, y)] == tot_ones:  # IMPORTANT!!!
                min_dist = min(min_dist, dd[(x, y)])

        return -1 if min_dist == float('inf') else min_dist

        

        ## S1: BFS
        ## From houses to empty land
        ## T: O((M*N)^2)
        ## S: O(MN)

        if not grid or not grid[0]: return -1
        m, n = len(grid), len(grid[0])
        dd = defaultdict(int)  # Stores the dist sum at each 0 cell to the 1 cells (buildings)
        num_ones = defaultdict(int)  # Stores how many buildings visited 0 cell (x, y)
        
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



        ## S3: BFS
        ## T: O((M*N)^2)
        ## S: O(MN)

        m, n = len(grid), len(grid[0])
        queue = deque()
        total_buildings = 0
      
        # Data structures to keep count of how many buildings each empty land can reach
        reach_count = [[0] * n for _ in range(m)]      
        # Data structures to keep track of total distances from each empty land to all buildings
        distance_sum = [[0] * n for _ in range(m)]
      
        # Loop through each cell in the grid
        for i in range(m):
            for j in range(n):
                # If the cell is a building, perform a BFS from this building
                if grid[i][j] == 1:
                    total_buildings += 1
                    queue.append((i, j))
                    level_distance = 0
                    visited = set()
                    while queue:
                        # Increase the distance level by 1 for each level of BFS
                        level_distance += 1
                      
                        # Loop through each cell in the current BFS level
                        for _ in range(len(queue)):
                            r, c = queue.popleft()
                            # Explore the four directions around the current cell
                            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                                x, y = r + dr, c + dc
                                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not in visited:
                                    # Increment the building reach count and add the distance
                                    reach_count[x][y] += 1
                                    distance_sum[x][y] += level_distance
                                  
                                    # Add the cell to the queue and mark it as visited
                                    queue.append((x, y))
                                    visited.add((x, y))
      
        # Set an initial answer as infinity to find the minimum
        answer = float('inf')
      
        # Loop to find the minimum distance of an empty land cell that can reach all buildings
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach_count[i][j] == total_buildings:
                    answer = min(answer, distance_sum[i][j])
      
        # If no cell can reach all buildings, return -1; otherwise, return the minimum distance
        return -1 if answer == float('inf') else answer
        