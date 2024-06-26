class Solution:
    def minJumps(self, arr: List[int]) -> int:
        from collections import defaultdict, deque

        ## S1: BFS
        ## Time: O(N+E), N = len(arr) and E is the total number of edges with equal values
        ## Space: O(N)
        n = len(arr)
        if n == 1: return 0
        d = defaultdict(list)
        for i, v in enumerate(arr):
            d[v].append(i)
        
        q = deque([(0, 0)]) # (original index, steps)
        visited = set([0])

        while q:
            i, steps = q.popleft()
            if i == n - 1:
                return steps
            
            steps += 1
            v = arr[i]
            for j in [i - 1, i + 1] + d[v]:
                if j < 0 or j >= n:
                    continue
                if j in visited:
                    continue
                visited.add(j)
                q.append((j, steps))
            
            del d[v]
        return -1
        
        """
        ## S2: Bidirection BFS
        ## T: O(N)
        ## S: O(N)

        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = set([0])  # store layers from start
        visited = {0, n-1}
        step = 0

        other = set([n-1]) # store layers from end

        # when current layer exists
        while curs:
            # search from the side with fewer nodes
            if len(curs) > len(other):
                curs, other = other, curs
            nex = set()

            # iterate the layer
            for node in curs:

                # check same value
                for child in graph[arr[node]]:
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.add(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if child in other:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.add(child)

            curs = nex
            step += 1

        return -1
        """