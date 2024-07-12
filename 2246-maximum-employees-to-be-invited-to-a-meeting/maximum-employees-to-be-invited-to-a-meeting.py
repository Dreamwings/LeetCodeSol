class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        from collections import deque

        ## S1: Topological Sort
        ## T: O(N) for both functions
        ## S: O(N) for both functions

        # Helper function to find the length of the largest cycle
        def max_cycle(favorites):
            n = len(favorites)
            visited = [False] * n
            max_ans = 0

            # Iterate over all students
            for i in range(n):
                if visited[i]:
                    continue
                cycle = []
                j = i
                # Build the cycle starting from student i
                while not visited[j]:
                    cycle.append(j)
                    visited[j] = True
                    j = favorites[j]

                # Detect the cycle length
                for k, v in enumerate(cycle):
                    if v == j:
                        max_ans = max(max_ans, len(cycle) - k)
                        break
            return max_ans

        # Helper function to perform topological sort and find the longest path in the graph
        def topo_sort(favorites):
            n = len(favorites)
            indeg = [0] * n
            longest = [1] * n
            # Create indegree array
            for v in favorites:
                indeg[v] += 1
            # Queue for zero indeg students
            q = deque([i for i, d in enumerate(indeg) if d == 0])

            # Perform BFS
            while q:
                x = q.popleft()
                longest[favorites[x]] = max(longest[favorites[x]], longest[x] + 1)
                indeg[favorites[x]] -= 1
                if indeg[favorites[x]] == 0:
                    q.append(favorites[x])

            # Sum the distances of mutually favorite pairs
            return sum(longest[i] for i, v in enumerate(favorites) if i == favorites[favorites[i]])

        # Return the maximum value among the longest cycle and the result of the topological sort
        return max(max_cycle(favorite), topo_sort(favorite))
