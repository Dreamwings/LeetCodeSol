class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        from collections import defaultdict, deque

        ## S1: Recursive DFS

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        seen = [False] * n
        
        def dfs(node):
            if node == destination:
                return True
            if not seen[node]:
                seen[node] = True
                for next_node in graph[node]:
                    if dfs(next_node):
                        return True
            return False
            
        return dfs(source)



        ## S2: BFS

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Store all the nodes to be visited in 'queue'.
        seen = [False] * n
        seen[source] = True
        q = deque([source])
    
        while q:
            x = q.popleft()
            if x == destination:
                return True

            # For all the neighbors of the current node, if we haven't visit it before,
            # add it to 'q' and mark it as visited.
            for y in graph[x]:
                if not seen[y]:
                    seen[y] = True
                    q.append(y)
        
        return False