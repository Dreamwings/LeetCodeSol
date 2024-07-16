class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        ## S2: DFS
        ## T: O(N + E)
        ## S: O(N)

        # Get the number of nodes in the graph
        n = len(graph)
        # Initialize a list to store the status of the nodes
        # Color 0 means unvisited, 1 means visiting, 2 means safe
        colors = [0] * n
        
        # Helper function to perform a depth-first-search (dfs) 
        # to determine if a node leads to a cycle (not safe) or not.
        def dfs(x):
            # If the node is already visited, return True if it is safe (color 2)
            if colors[x]:
                return colors[x] == 2
            # Mark this node as visited (color 1)
            colors[x] = 1
            # Traverse all connected nodes (neighbors) to see if they lead to a cycle
            for y in graph[x]:
                # If a connected node is not safe, then this node is also not safe
                if not dfs(y):
                    return False
            # If all connected nodes are safe, mark this node as safe (color 2)
            colors[x] = 2
            return True

        # Use list comprehension to gather all nodes that are safe after DFS
        # These are the eventual safe nodes that do not lead to any cycles
        return [x for x in range(n) if dfs(x)]


## S1: Topological Sort
## T: O(N + E)
## S: O(N + E)

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        adj = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1

        q = deque()
        # Push all the nodes with indegree zero in the queue.
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True

            for neighbor in adj[node]:
                # Delete the edge "node -> neighbor".
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        safeNodes = []
        for i in range(n):
            if safe[i]:
                safeNodes.append(i)

        return safeNodes