class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        from collections import defaultdict, deque
        
        ## S 1: Topological Sort (BFS with In Degree)
        ## Time: O(N + E), N is num of vertexes, E is num of edges
        ## Space: O(N + E)
        
        # build the graph
        graph = defaultdict(list)
        indeg = {x: 0 for x in range(numCourses)}
        
        for u, v in prerequisites: 
            # u <- v, v must be taken before u
            graph[v].append(u)
            indeg[u] += 1
        
        q = deque()
        visited = set()
        
        for x in indeg:
            if indeg[x] == 0:
                # Add courses to be taken first into q
                q.append(x)
        
        if not q: return False # There is a loop
        
        while q:
            x = q.popleft()
            visited.add(x)
            for y in graph[x]:
                indeg[y] -= 1
                if indeg[y] == 0:
                    q.append(y)
        
        if len(visited) == numCourses:
            return True
        return False
        
        
        
        ## S 2: DFS
        ## https://leetcode-cn.com/problems/course-schedule/solution/ke-cheng-biao-by-leetcode-solution/
        ## Time: O(N + E)
        ## Space: O(N + E)
        
        graph = defaultdict(list)
        visited = [0] * numCourses
        # a node x has 3 status visited[x]:
        # 0 : not visited
        # -1: is being visited in a DFS search, if you meet it again, it means there is a loop, 
        # so you can't make the topological sorting
        # 1 : visited, 
        
        for u, v in  prerequisites:
            graph[u].append(v)
            
        
        def dfs(i):
            # print(i, visited[i])
            if visited[i] == -1: return False # There is a loop
            if visited[i] == 1: return True
            
            visited[i] = -1  # temperorily set it to unvisited
            
            for x in graph[i]:
                if not dfs(x):
                    return False
            
            visited[i] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        
        