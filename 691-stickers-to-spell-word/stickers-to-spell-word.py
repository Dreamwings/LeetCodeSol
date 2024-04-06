class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        ## S4: DFS
        ## T: O(M* 2^N)

        stickers = [collections.Counter(s) for s in stickers if set(s) & set(target)]
        self.map = {}

        def dfs(target):
            if not target: 
                return 0
            if target in self.map: 
                return self.map[target]

            cnt, res = collections.Counter(target), float('inf')

            for c in stickers: # traverse the stickers to get new target
                if c[target[0]] == 0: 
                    # we can make sure the 1st letter will be removed to reduce the time complexity
                    continue 
                nxt = dfs(''.join([s * t for (s, t) in (cnt - c).items()]))
                if nxt != -1: 
                    res = min(res, 1 + nxt)
            self.map[target] = -1 if res == float('inf') else res
            return self.map[target]

        return dfs(target)
        
        """
        ## S3: DFS with Memory

        @lru_cache(None)
        def dfs(target):
            if not target: return 0
            tCtr, res = Counter(target), inf
            mn = min(tuple(tCtr), key= lambda x: tCtr[x] )

            for sCtr in sCtrs: 
                if sCtr[mn] == 0: continue 
                nxt = dfs(''.join((tCtr-sCtr).elements()))
                
                if nxt != -1: res = min(res, 1 + nxt)
            
            return -1 if res == inf else res

        sCtrs = list(filter(lambda s: bool(set(s) & set(target)), map(Counter, stickers)))
        
        return dfs(target)

        
        ## S2: DP
        ## T: O(2^N * M * L) 
        ## S: O(2^N)

        n = len(target)
        dp = [-1] * (1 << n) # 2^n states
        dp[0] = 0
        for k in range(1 << n):
            if dp[k] == -1: continue
            for sticker in stickers:
                now = k
                for letter in sticker:
                    for i in range(n):
                        if (now >> i) & 1: continue
                        if target[i] == letter:
                            now |= 1 << i
                            break
                if dp[now] == -1 or dp[now] > dp[k] + 1:
                    dp[now] = dp[k] + 1
        return dp[-1]
        
        
        ## S1: BFS from AlgoMonster
        ## T: O(2^N * M * L * K) 
        ## S: O(2^N)

        queue = deque([0])
        # Initialize the number of steps (minimum stickers) to 0.
        steps = 0
        # Calculate the length of the target word.
        n = len(target)
        # Create a visited states list to prevent repeated processing of the same state.
        visited = [False] * (1 << n)
        # Mark the empty state as visited.
        visited[0] = True  
      
        # Start the breadth-first search.
        while queue:
            # Process all the states at the current level.
            for _ in range(len(queue)):
                current_state = queue.popleft()
              
                # If all characters are used, return the number of steps.
                if current_state == (1 << n) - 1:
                    return steps
              
                # Try all stickers for the current state.
                for sticker in stickers:
                    next_state = current_state
                    sticker_count = Counter(sticker)
                  
                    # Attempt to match sticker characters with target characters.
                    for i, char in enumerate(target):
                        # If the character at position i is not yet added, and the sticker has the char.
                        if not (next_state & (1 << i)) and sticker_count[char]:
                            next_state |= 1 << i
                            sticker_count[char] -= 1
                          
                    # If the next state has not been visited, mark it as visited and add to the queue.
                    if not visited[next_state]:
                        visited[next_state] = True
                        queue.append(next_state)
          
            # Increment the step count after processing all states at the current level.
            steps += 1
      
        # If target cannot be reached return -1 indicating not possible.
        return -1
        
        """
        