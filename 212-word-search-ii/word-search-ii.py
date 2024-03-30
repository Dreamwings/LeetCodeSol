class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        ## S2: Backtracking with Trie
        ## T:
        ## S:

        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(x, y, parent):    
            
            letter = board[x][y]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited 
            board[x][y] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (dx, dy) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                i, j = x + dx, y + dy     
                if i < 0 or i >= rowNum or j < 0 or j >= colNum:
                    continue
                if not board[i][j] in currNode:
                    continue
                backtracking(i, j, currNode)    
        
            # End of EXPLORATION, we restore the cell
            board[x][y] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)    


        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords            
        
        
        """
        ## S1: Improved DFS Backtracking (Time Limit Exceeded)
        
        ## add Counter for both board and each word
        ## for a char c, if a word has more c than the board, don't do DFS
        
        from collections import Counter
        
        m, n = len(board), len(board[0])
        
        def dfs(word, pos, x, y, seen):
            if pos == len(word):
                return True
            
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            
            if (x, y) in seen or word[pos] != board[x][y]:
                return False
            
            dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            seen.add((x, y))
            for dx, dy in dir:
                i, j = x + dx, y + dy
                if dfs(word, pos + 1, i, j, seen):
                    return True
            seen.remove((x, y))
            return False
        
        bc = Counter() 
        for r in board:
            rc = Counter(r)
            bc += rc # Note that you can merge two Counters a and b by a + b directly
        
        res = []
        wset = set(words)
        
        # first check if board contains all chars in the word w
        # if not, remove the word from word set
        for w in words:
            wc = Counter(w)
            for k, v in wc.items():
                if v > bc[k] and w in wset:
                    wset.remove(w)
                    break
        
        # if board contains all chars in w, do DFS backtracking
        for w in wset:
            found = False
            for i in range(m):
                for j in range(n):
                    if w[0] == board[i][j]:
                        seen = set()
                        if dfs(w, 0, i, j, seen):
                            res.append(w)
                            found = True
                            break
                if found:
                    break
        
        return res
        """