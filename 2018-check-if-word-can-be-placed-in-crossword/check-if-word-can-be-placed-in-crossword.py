class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
        ## S1:
        ## T: O(M * N * K), K = len(word)
        ## S: O(M * N)

        n = len(word)
        
        for mat in board, list(zip(*board)):
            for row in mat:
                arr = "".join(row).split("#")
                # print("".join(row), arr)
                for s in arr:
                    for w in [word, word[::-1]]:
                        if len(s) == n and all(s[i] == w[i] or s[i] == " " for i in range(n)):
                            return True
        return False
        


        ## S2: DFS + Cache
        ## T: O(M * N * K), K = len(word)
        ## S: O(M * N)

        m, n = len(board), len(board[0])
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        
        @lru_cache(maxsize=None)
        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n and board[r][c] != '#'
        
        @lru_cache(maxsize=None)
        def dfs(i, r, c, dr, dc):
            if i == len(word):
                return not is_valid(r, c)
            
            if not is_valid(r, c) or board[r][c] not in [' ', word[i]]:
                return False
            
            rr, cc = r + dr, c + dc            
            return dfs(i+1, rr, cc, dr, dc)
        
        
        for r in range(m):
            for c in range(n):
                for dr, dc in dirs:
                    x, y = r - dr, c - dc # previous (r, c)
                    if not is_valid(x, y) and dfs(0, r, c, dr, dc):
                        return True
                    
        return False

        