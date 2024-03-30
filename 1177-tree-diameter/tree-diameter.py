class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        ## S2: DFS
        ## T: O(N)
        ## S: O(N)

        # build the adjacency list representation of the graph.
        graph = [set() for i in range(len(edges)+1)]
        for edge in edges:
            u, v = edge
            graph[u].add(v)
            graph[v].add(u)

        diameter = 0

        def dfs(curr, visited):
            # return the max distance
            # starting from the 'curr' node to its leaf nodes
            
            nonlocal diameter

            # the top 2 distance starting from this node
            top_1_distance, top_2_distance = 0, 0

            distance = 0
            visited[curr] = True

            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    distance = 1 + dfs(neighbor, visited)

                if distance > top_1_distance:
                    top_1_distance, top_2_distance = distance, top_1_distance
                elif distance > top_2_distance:
                    top_2_distance = distance

            # with the top 2 distance, we can update the current diameter
            diameter = max(diameter, top_1_distance + top_2_distance)

            return top_1_distance

        visited = [False for i in range(len(graph))]
        dfs(0, visited)

        return diameter

        """
        ## S1: BFS
        ## T: O(N)
        ## S: O(N)

        # build the adjacency list representation of the graph
        graph = [set() for i in range(len(edges)+1)]
        for edge in edges:
            u, v = edge
            graph[u].add(v)
            graph[v].add(u)

        def bfs(start):
            # return the farthest node from the 'start' node
            # and the distance between them.
            
            visited = [False] * len(graph)

            visited[start] = True
            queue = deque([start])
            distance = -1
            last_node = start
            while queue:
                next_queue = deque()
                while queue:
                    next_node = queue.popleft()
                    for neighbor in graph[next_node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            next_queue.append(neighbor)
                            last_node = neighbor
                distance += 1
                queue = next_queue

            return last_node, distance

        # 1). find one of the farthest nodes
        farthest_node, distance_1 = bfs(0)
        # 2). find the other farthest node
        #  and the distance between two farthest nodes
        another_farthest_node, distance_2 = bfs(farthest_node)

        return distance_2

        """