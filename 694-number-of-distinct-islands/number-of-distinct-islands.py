class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        """
        ## S1: DFS
        ## T: O(M * N)
        ## S: O(M * N)

        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        islands = set()
        
        def dfs(x, y, sx, sy, q):
            d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            grid[x][y] = 0
            q.add(((x - sx), (y - sy)))
            
            for dx, dy in d:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and grid[i][j]:
                    dfs(i, j, sx, sy, q)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    q = set()
                    dfs(i, j, i, j, q)
                    islands.add(tuple(q))
        
        return len(islands)
        
        """
        ## S2:

        islands = set()
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r: int , c: int):
            nonlocal islands
            temp_islands = set()
            initial = (r,c), (0,0)
            line = [initial]
            
            def add_to_line(row: int , col: int, cur_x: int, cur_y: int):
                nonlocal line, temp_islands
                if (row < 0) or (row >= rows) or (col < 0) or (col >= cols) or grid[row][col] == 0:
                    return
                reference = (cur_x, cur_y)
                to_add = (row, col), reference
                line.append(to_add)
                temp_islands.add(reference)
                grid[row][col] = 0
            
            for cord, reference in line:
                cur_row, cur_col = cord
                x, y = reference
                
                add_to_line(cur_row + 1, cur_col, x + 1, y)
                add_to_line(cur_row - 1, cur_col, x - 1, y)
                add_to_line(cur_row, cur_col + 1, x, y + 1)
                add_to_line(cur_row, cur_col - 1, x, y - 1)
                
            island = tuple(temp_islands)
            islands.add(island)
                
        for single_row in range(rows):
            for single_col in range(cols):
                if grid[single_row][single_col] == 1:
                    bfs(single_row, single_col)
        
        return len(islands)
