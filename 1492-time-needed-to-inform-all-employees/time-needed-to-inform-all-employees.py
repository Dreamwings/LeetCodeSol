class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        ## S1: DFS
        ## T: O(N)
        ## S: O(N)

        # Recursive DFS function to calculate the time taken to inform each employee.
        def dfs(employee_id: int) -> int:
            max_time = 0
            for x in graph[employee_id]:
                # Recursively call dfs for the subordinate and add the current employee's inform time.
                # We want the maximum time required for all subordinates as they can be informed in parallel.
                max_time = max(max_time, dfs(x) + informTime[employee_id])
            return max_time

        # Create a graph where each employee is a node and the edges are from managers to subordinates.
        graph = defaultdict(list)
        for i, mng_id in enumerate(manager):
            # Skip the head of the company as they have no manager.
            if mng_id != -1:
                graph[mng_id].append(i)

        # Kick off the dfs from the head of the company to calculate the total time required.
        return dfs(headID)



        ## S2: BFS
        ## T: O(N)
        ## S: O(N)

        q = collections.deque([(headID, 0)])
        subordinates = collections.defaultdict(list)
        res = 0
        for i, v in enumerate(manager):
            subordinates[v].append(i)
            
        while q:
            u, time = q.popleft()
            res = max(res, time)
            for v in subordinates[u]:
                q.append((v, time + informTime[u]))
        return res



        ## S3: Dijkstra
        ## T: O(Elog(V)) = O(Vlog(V)), E = V - 1
        ## S: O(V)

        graph = collections.defaultdict(list)
        
        for i, managerId in enumerate(manager):
            graph[managerId].append((informTime[i], i))
        
        dist = {}
        heap = [(informTime[headID], headID)] 
        
        while heap:
            time, u = heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = time    
            for w, v in graph[u]:
                if v in dist:
                    continue
                heapq.heappush(heap, (time+w, v))    
        return max(dist.values())         