class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ## S2: BFS (Time Limit Exceeded)
        ## T: O(N^2)
        ## S: O(N^2)
        
        n = len(grid)
        if grid[0][0] == 1: return -1

        q = collections.deque()
        q.append((0, 0, 1))
        d = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        grid[0][0] = 1 # Mark this cell as visited using 1

        while q:
            x, y, steps = q.popleft()
            if x == y == n - 1:
                return steps
            
            for dx, dy in d:
                i, j = x + dx, y + dy
                if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                    q.append((i, j, steps + 1))
                    grid[i][j] = 1 # Mark this cell as visited using 1

        return -1

        """

        ## S3: A* Algorithm 
        ## https://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
        ## https://www.redblobgames.com/pathfinding/a-star/introduction.html
        ## T: O(N^2 * log(N^2))
        ## S: O(N^2)
        
        from heapq import heappush, heappop

        n = len(grid)
        if grid[0][0] == 1: return -1
        d = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        def get_neighbors(x, y):
            for dx, dy in d:
                i, j = x + dx, y + dy
                if not(0 <= i < n and 0 <= j < n):
                    continue
                if grid[i][j] != 0:
                    continue
                yield (i, j)

        # Helper function for the A* heuristic.
        def best_estimate(row, col):
            return max(n - 1 - row, n - 1 - col)

        # Set up the A* search.
        visited = set()
        # Entries on the priority queue are of the form
        # (total distance estimate, distance so far, (cell row, cell col))
        hq = [(1 + best_estimate(0, 0), 1, (0, 0))]

        while hq:
            est, dist, cell = heappop(hq)
            if cell in visited:
                continue
            if cell == (n - 1, n - 1):
                return dist
            
            visited.add(cell)

            for neighbor in get_neighbors(*cell):
                # The check here isn't necessary for correctness, but it
                # leads to a substantial performance gain.
                if neighbor in visited:
                    continue
                new_est = best_estimate(*neighbor) + dist + 1
                heappush(hq, (new_est, dist + 1, neighbor))

        return -1


        ## S1: BFS
        ## T: O(N^2)
        ## S: O(N^2)

        n = len(grid)
        if grid[0][0] == 1: return -1
        
        q = [(0, 0)]
        grid[0][0] = 1
        steps = 0
        d = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        while q:
            nxt = []
            steps += 1
            for x, y in q:
                if x == y == n - 1:
                    return steps

                for dx, dy in d:
                    i, j = x + dx, y + dy
                    if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                        nxt.append((i, j))
                        grid[i][j] = 1
            q = nxt
            
        return -1            
        
        """
