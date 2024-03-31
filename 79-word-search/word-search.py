class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ## S1: DFS Backtracking
        ## T: O(M*N*3^L), L = len(word)
        ## S: O(L)
        m, n = len(board), len(board[0])
        
        def dfs(pos, x, y):
            if pos == len(word) - 1:
                return board[x][y] == word[pos]
            
            if board[x][y] != word[pos]:
                return False
                
            tmp, board[x][y] = board[x][y], "#"
            dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            for dx, dy in dir:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and board[i][j] != "#":
                    if dfs(pos + 1, i, j):
                        return True
            
            board[x][y] = tmp
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True
        
        return False
            
        """
        
        m, n = len(board), len(board[0])
        
        def dfs(word, x, y):
            if len(word) == 0: return True
            if x < 0 or x >= m or y < 0 or y >= n or word[0] != board[x][y]:
                return False
            
            tmp, board[x][y] = board[x][y], '*'  ## Mark visited cell
            
            d1 = dfs(word[1:], x + 1, y)
            d2 = dfs(word[1:], x, y + 1)
            d3 = dfs(word[1:], x - 1, y)
            d4 = dfs(word[1:], x, y - 1)
            
            board[x][y] = tmp
            
            return d1 or d2 or d3 or d4
        
        for i in range(m):
            for j in range(n):
                if dfs(word, i, j):
                    return True
        
        return False
        
        """
        