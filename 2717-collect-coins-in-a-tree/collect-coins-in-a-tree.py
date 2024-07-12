class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        from collections import deque

        ## S1: Topological Sort
        ## T: O(N)
        ## S: O(N)

        # Create a graph represented as an adjacency list
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
      
        n = len(coins)
      
        # Queue for BFS, initialized with leaf nodes having 0 coins
        # q = deque([node for node in range(n) if len(graph[node]) == 1 and coins[node] == 0])
        q = deque()
        for node in range(n):
            if len(graph[node]) == 1 and coins[node] == 0:
                q.append(node)
      
        # Process nodes with BFS approach
        while q:
            x = q.popleft()
            for y in graph[x]: # Look at neighbors of x
                graph[y].remove(x)  # Remove the edge to the x node
                if coins[y] == 0 and len(graph[y]) == 1:
                    q.append(y)  # Add leaf neighbors with 0 coins to the q
            graph[x].clear()  # Clear the edges of the x node
     
        # Repeat the edge-clearing process twice
        for _ in range(2):
            # Find all nodes with exactly one connection
            one_conn = [node for node in range(n) if len(graph[node]) == 1]
            for node in one_conn:
                for neighbor in graph[node]:
                    graph[neighbor].remove(node)  # Remove the edge
                graph[node].clear()  # Clear the edges of the node
      
        # Count the remaining edges after clearing, and multiply by 2 since each edge is counted twice
        res = sum(len(graph[a]) > 0 and len(graph[b]) > 0 for a, b in edges) * 2
      
        return res