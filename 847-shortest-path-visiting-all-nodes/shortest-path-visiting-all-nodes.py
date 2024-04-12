class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        ## S1: BFS
        ## T: O(N * 2^N)
        ## S: O(N * 2^N)

        n = len(graph)  # Number of nodes in the graph
        queue = deque()
        visited = set()  # Set to store visited (node, state) tuples
      
        # Initialize the queue and visited set with all individual nodes and their bitmasks
        for node in range(n):
            state = 1 << node
            queue.append((node, state))
            visited.add((node, state))
      
        ending_state = (1 << n) - 1
        steps = 0
      
        while queue:
            # Iterate over nodes in the current layer
            for _ in range(len(queue)):
                x, state = queue.popleft()
                
                if state == ending_state:
                    return steps
              
                # Explore neighbors of the current node
                for y in graph[x]:
                    new_state = state | (1 << y)
                    # If the new state has not been visited, add it to the queue and set
                    if (y, new_state) not in visited:
                        visited.add((y, new_state))
                        queue.append((y, new_state))
          
            # After exploring all nodes at the current depth, increment steps
            steps += 1

        """

        ## S2: DFS + Memoization (Top-Down DP)
        ## T: O(2^N * N^2), 2^N * N possible states, and N nodes
        ## S: O(2^N * N)


        def dp(node, mask):
            state = (node, mask)
            if state in cache:
                return cache[state]
            if mask & (mask - 1) == 0:
                # Base case - mask only has a single "1", which means
                # that only one node has been visited (the current node)
                return 0

            cache[state] = float("inf") # Avoid infinite loop in recursion
            for neighbor in graph[node]:
                if mask & (1 << neighbor):
                    already_visited = 1 + dp(neighbor, mask)
                    not_visited = 1 + dp(neighbor, mask ^ (1 << node))
                    cache[state] = min(cache[state], already_visited, not_visited)

            return cache[state]

        n = len(graph)
        ending_mask = (1 << n) - 1
        cache = {}

        return min(dp(node, ending_mask) for node in range(n))

        """