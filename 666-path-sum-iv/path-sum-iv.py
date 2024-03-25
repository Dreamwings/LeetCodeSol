class Solution:
    def pathSum(self, nums: List[int]) -> int:
        
        ## S1: DFS
        ## T: O(N)
        ## S: O(H)
        ans = 0
        mp = {num // 10: num % 10 for num in nums}

        def dfs(node, t):
            if node not in mp:
                return
            t += mp[node]
            d, p = divmod(node, 10)
            l = (d + 1) * 10 + (p * 2) - 1
            r = l + 1
            nonlocal ans
            if l not in mp and r not in mp:
                ans += t
                return
            dfs(l, t)
            dfs(r, t)

        dfs(11, 0)
        return ans

        """
        ## S2: 
        ## 假设某Node前两位数为xy，则其parent node前两位数为:
        ## (x - 1) * 10 + (y + 1) / 2
        
        d = collections.defaultdict(int)
        d = {1 : 0}
        leaves = set([1])
        for num in nums:
            path, val = num // 10, num % 10
            x, y = path // 10, path % 10
            parent = (x - 1) * 10 + (y + 1) // 2
            d[path] = d[parent] + val
            leaves.add(path)
            if parent in leaves: 
                leaves.remove(parent)

        return sum(d[v] for v in leaves)        

        """
