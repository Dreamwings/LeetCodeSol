class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        
        ## S1: DFS + BFS
        ## N nodes, E edges
        ## T: O(N + E) + O(N * (N + E)) ~ O(N * (N + E))
        ## S: O(N + E)

        # Depth-first search function to explore all the nodes within a connected component
        def dfs(x):
            group.append(x)
            visited[x] = True
            for y in graph[x]:
                if not visited[y]:
                    dfs(y)

        # Breadth-first search function to calculate the maximum distance from the start node
        def bfs(start_node):
            max_dist = 1
            d = [float('inf')] * (n + 1) # To store distances
            d[start_node] = 1
            q = collections.deque([start_node])
          
            while q:
                x = q.popleft()
                for y in graph[x]:
                    if d[y] == float('inf'):
                        max_dist = d[y] = d[x] + 1
                        q.append(y)
          
            # Assign an incremental distance value for disconnected nodes in the component
            for node in group:
                if d[node] == float('inf'):
                    max_dist += 1
                    d[node] = max_dist
          
            # Verify the resultant d conform to the problem constraints
            for x in group:
                for y in graph[x]:
                    if abs(d[x] - d[y]) != 1:
                        return -1
            return max_dist

        # Initialize an adjacency list graph and visited list
        graph = defaultdict(list)
        for edge in edges:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)
      
        visited = [False] * (n + 1)
        total_sets = 0

        # Traverse all nodes to find disconnected components
        for i in range(1, n + 1):
            if not visited[i]:
                group = []
                dfs(i)  # DFS to populate group
              
                # Perform BFS on all nodes in the component and find the maximum distance
                max_dist = max(bfs(node) for node in group)
              
                if max_dist == -1:
                    return -1  # Early return if any component doesn't fulfill the requirements
              
                total_sets += max_dist
      
        # Return the total potential magnificent sets across all components
        return total_sets
