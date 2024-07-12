class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        
        ## S1: DFS
        ## T: O(E) + O(1) + O(N) * O(N) ~ O(N^2)
        ## S: O(N^2) for the worst case of stack

        # Build the graph from the edges
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        # Precompute coprimes for numbers from 1 to 50
        coprimes = defaultdict(list)
        for i in range(1, 51):
            for j in range(1, 51):
                if math.gcd(i, j) == 1:
                    coprimes[i].append(j)

        # Initialize stacks to keep track of res' values
        stacks = defaultdict(list)
        # Initialize the list to store res for each node
        res = [-1] * len(nums)

        # Function to execute Depth-First Search (DFS)
        def dfs(cur, parent, depth):
            closest = -1 # closest coprime ancestor
            max_depth = -1
            for v in coprimes[nums[cur]]:
                stack = stacks[v]
                if stack and stack[-1][1] > max_depth:
                    closest, max_depth = stack[-1]
            res[cur] = closest
            for neighbor in graph[cur]:
                if neighbor != parent:
                    stacks[nums[cur]].append((cur, depth))
                    # Recursive DFS call
                    dfs(neighbor, cur, depth + 1)
                    # Pop the element when backtracking
                    stacks[nums[cur]].pop()


        # Start DFS from the root node, here considered to be node 0
        dfs(0, -1, 0)
      
        # Return the final list of res
        return res