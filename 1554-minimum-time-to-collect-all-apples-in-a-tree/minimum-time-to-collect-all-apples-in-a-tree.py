class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        ## S1: DFS

        # Construct the graph using adjacency lists.
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
      
        visited = set()

        def dfs(node, cost_to_come_back):
            # If the current node has been visited, no need to do anything.
            if node in visited:
                return 0
            visited.add(node)
          
            # Accumulated cost of visiting children nodes.
            total_cost = 0
            for child in graph[node]:
                # Perform DFS on child nodes with the cost of coming back (2 units).
                total_cost += dfs(child, 2)
          
            # If there's no apple at the current node, and no cost accumulated from children,
            # it means we don't need to collect any apples on this path.
            if not hasApple[node] and total_cost == 0:
                return 0
          
            # Return the total cost of picking apples from this subtree (including the cost to come back).
            return cost_to_come_back + total_cost

      
        # Perform a DFS starting at node 0 with no initial cost.
        # Since we start at the root and don't need to return, we pass 0 as the cost.
        return dfs(0, 0)


