class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        ## S1: DFS
        ## T: O(N + E), N is num of nodes, E is num of edges
        ## Each node triggers the DFS call at most once, and each edge is considered once across all DFS calls. 
        ## S: O(N)

        # This method finds the quietest person in the group or among their richer acquaintances.
        # Build the graph given the richer relationship.
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
      
        # Initialize the res list with -1 for all persons.
        n = len(quiet)
        res = [-1] * n
      
        # Depth-first search to update the res for each person.      
        def dfs(x):
            # x is the index of the current person
            if res[x] != -1:
                # If this person's res is already calculated, return.
                return
            # Otherwise, initialize this person's res as themselves.
            res[x] = x
            for y in graph[x]: # y is the neighbor, visit all richer neighbors.
                dfs(y)
                # If the y has found someone quieter, update this person's res.
                if quiet[res[y]] < quiet[res[x]]:
                    res[x] = res[y]

        # Perform dfs for each person.
        for i in range(n):
            dfs(i)

        # Return the completed res list.
        return res
