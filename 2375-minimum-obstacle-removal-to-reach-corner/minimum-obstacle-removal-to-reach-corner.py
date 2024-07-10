class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        ## S1: BFS
        ## T: O(MN)
        ## S: O(MN)

        from collections import deque
        from itertools import pairwise

        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])
        q = deque([(0, 0, 0)])  # (x, y, obstacle_cnt)
        visited = set() # Create a set to keep track of visited cells
      
        # Define the directions to move in the grid, pairwise will use this
        dir = (-1, 0, 1, 0, -1)
      
        # Loop until we find the exit or run out of cells to explore
        while q:
            # Pop the cell from the q and count of obstacles encountered so far
            x, y, cnt = q.popleft()
          
            # If we've reached the bottom right corner, return the obstacle count
            if x == m - 1 and y == n - 1:
                return cnt
          
            # If this cell has been visited before, skip to the next iteration
            if (x, y) in visited:
                continue
          
            visited.add((x, y)) # Mark the current cell as visited
          
            # Iterate over all possible moves (up, down, left, right)
            for dx, dy in pairwise(dir):
                i, j = x + dx, y + dy
              
                # Check if the new position is within bounds
                if 0 <= i < m and 0 <= j < n:
                    # If there is no obstacle, add the cell to the front of the q to explore it next
                    if grid[i][j] == 0:
                        q.appendleft((i, j, cnt))
                    # If there is an obstacle, add the cell to the back of the q with the obstacle count incremented
                    else:
                        q.append((i, j, cnt + 1))
