class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ## S1: BFS
        ## T: O(N^2)
        ## S: O(N^2)
        n = len(grid)
        if grid[0][0] == 1: return -1
        
        q = [(0, 0)]
        grid[0][0] = 1
        res = 0
        d = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        while q:
            nxt = []
            res += 1
            for x, y in q:
                if x == y == n-1:
                    return res
                for dx, dy in d:
                    i, j = x + dx, y + dy
                    if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                        nxt.append((i, j))
                        grid[i][j] = 1
            q = nxt
            
        return -1            
        
        
        