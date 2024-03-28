class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        ## S1: BFS
        ## T: O(M^2 * K)
        ## S: O(M*K)
        
        from collections import defaultdict
        
        d = defaultdict(set)
        
        for i, r in enumerate(routes):
            for x in r:
                d[x].add(i)
                
        q = [(source, 0)]
        seen = set([source])
        
        for x, cnt in q:
            if x == target:
                return cnt
            for i in d[x]:
                for y in routes[i]:
                    if y not in seen:
                        q.append((y, cnt + 1))
                        seen.add(y)
                routes[i] = []
                
        return -1