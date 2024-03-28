class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        from collections import defaultdict, deque
        
        ## Solution 1: BFS/Topological Sort
        ## T: O(V+E)
        ## S: O(V+E)
        
        g = defaultdict(list)
        indeg = {i: 0 for i in range(numCourses)}
        
        for x, y in prerequisites:
            g[y].append(x)
            indeg[x] += 1
        
        q = deque()
        
        for k, v in indeg.items():
            if v == 0:
                q.append(k)
        
        res = []
        if not q: return res
        
        while q:
            x = q.popleft()
            res.append(x)
            for y in g[x]:
                indeg[y] -= 1
                if indeg[y] == 0:
                    q.append(y)
       
        if len(res) == numCourses:
            return res
        return []
        
        """
        ## S2: DFS
        ## T: O(V+E)
        ## S: O(V+E)

        WHITE = 1
        GRAY = 2
        BLACK = 3

        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)

        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True

        # By default all vertces are WHITE
        color = {k: Solution.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return

            # Start the recursion
            color[node] = Solution.GRAY

            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                         # An edge to a GRAY vertex represents a cycle
                        is_possible = False

            # Recursion ends. We mark it as black
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []
        """