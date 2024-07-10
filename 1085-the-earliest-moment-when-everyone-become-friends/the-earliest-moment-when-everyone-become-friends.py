class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        ## S1: Union Find
        ## T: O(MlogM + MlogN), O(MlogM) for sorting logs, O(MlogN) for Union-Find
        ## S: O(N)

        uf = {x: x for x in range(n)}
        self.groups = n

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                self.groups -= 1
                uf[x] = y


        for t, x, y in sorted(logs):
            union(x, y)
            if self.groups == 1:
                return t
        return -1