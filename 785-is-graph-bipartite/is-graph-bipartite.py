class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        ## Solution 1: DFS
        ## T: O(V + E)
        ## S: O(V)
        
        color = {}
        def dfs(x):
            for y in graph[x]:
                if y in color:
                    if color[y] == color[x]:
                        return False
                else:
                    color[y] = 1 - color[x]
                    if not dfs(y):
                        return False
            return True
        
        for x in range(len(graph)):
            if x not in color:
                color[x] = 0
                if not dfs(x):
                    return False
        
        return True
        
        ## Solution 2: BFS
        
