class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ## S1: BFS
        ## T: O(M * N)
        ## S: O(M * N)
        from collections import deque
        
        m, n = len(grid), len(grid[0])
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = []
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    cnt += 1
        
        if cnt == 0: return 0
        if not q: return -1
        
        # do BFS to clear cell with 1            
        step = 0
        while q:
            next_level = []
            for x, y in q:
                for dx, dy in d:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        grid[i][j] = 2
                        next_level.append((i, j))
                        cnt -= 1
            step += 1
            q = next_level
            
        if cnt > 0: return -1
        else: return step - 1

        """

        ## S2: Recursive + Set

        if not grid:
            return 0
        fresh_coords = set()
        rotten_coords = set()
        rows = len(grid)
        cols = len(grid[0])

        def recursive(fresh_coords, rotten_coords, rows, cols):
            if not fresh_coords:
                return 0
            if not rotten_coords:
                return -1
            newly_rotten = set()
            
            # start finding newly rotten oranges
            for fresh in fresh_coords:
                for neighbor in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    x = fresh[0] + neighbor[0]
                    y = fresh[1] + neighbor[1]
                    if x >= 0 and x < rows and y >= 0 and y < cols and (x, y) in rotten_coords:
                        newly_rotten.add(fresh)
                                
            '''
            if there is no newly_rotten orange, it means there is no way to 
            reach the fresh ones; remember that we have already made 
            sure that there are fresh oranges in the grid by checking the 
            number of fresh ones at the start of the recursive function.
            '''
            if not newly_rotten:
                return -1
            else:
                for coords in newly_rotten:
                    fresh_coords.remove(coords)
                    rotten_coords.add(coords)
                    
                temp = recursive(fresh_coords, rotten_coords, rows, cols)
                if temp == -1:
                    return -1
                else:
                    return 1 + temp


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_coords.add((i, j))
                elif grid[i][j] == 2:
                    rotten_coords.add((i, j))
                    
        return recursive(fresh_coords, rotten_coords, rows, cols)


        """
        