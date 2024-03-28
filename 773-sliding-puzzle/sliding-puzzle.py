class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        ## S1: BFS

        from collections import deque
        dirs = {
            0: [1, 3], 
            1: [0, 2, 4], 
            2: [1, 5], 
            3: [0, 4], 
            4: [1, 3, 5], 
            5: [2, 4]
        }
        # Flatten the board to a single list and start the BFS queue with this initial state and move count of 0.
        state = list((*board[0], *board[1]))
        q = deque([(state, 0)])  # (current state, move count)
        visit = set()

        while q:
            state, count = q.popleft()
            if state == [1, 2, 3, 4, 5, 0]:
                return count

            i = state.index(0)  # Find the index of the blank space (0)
            for j in dirs[i]:
                cur = state[:]  # Create a copy of the current state
                cur[i], cur[j] = cur[j], 0  # Swap the blank space with the adjacent number
                
                cur_tuple = tuple(cur)  # Convert list to tuple for hashability
                if cur_tuple not in visit:
                    visit.add(cur_tuple)
                    q.append((cur, count + 1))
        
        return -1   

        """
        ## S2: A* Search Algorithm
        ## See: https://algo.monster/liteproblems/773

        ## S3: BFS

        def neighbors(x):
            d = {0:[1,3], 1:[0,2,4], 2:[1,5], 3:[0,4], 4:[1,3,5], 5:[2,4]}
            i = x.find('0')
            res = []
            for j in d[i]:
                t = list(x)
                t[i], t[j] = t[j], t[i]
                res += ''.join(t),
            return res
        
        start, target = ''.join(map(str,chain(*board))), '123450'
        q = deque([(start, 0)])
        seen = {start}
        while q:
            cur, h = q.popleft()
            if cur == target:
                return h
            for n in neighbors(cur):
                if n not in seen:
                    seen.add(n)
                    q += (n, h + 1),
                    
        return -1

        """