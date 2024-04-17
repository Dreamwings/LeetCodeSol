class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        from collections import defaultdict
        
        ## S1: DFS
        ## T: O(NKlogNK), N = len(accounts) and K is the max length of an account
        ## S: O(NK)

        ## Build a graph with master email address, then do DFS with master email and its neighbors
        def build_graph(accounts):
            graph = defaultdict(list)
            for a in accounts:
                for e in set(a[2:]):
                    graph[a[1]].append(e)
                    graph[e].append(a[1])
            return graph
        
        def dfs(e, graph, visited, emails):
            if e in visited:
                return
            
            visited.add(e)
            emails.append(e)

            for x in graph[e]:
                dfs(x, graph, visited, emails)
        
        graph = build_graph(accounts)
        visited = set()
        res = []

        for a in accounts:
            emails = []
            dfs(a[1], graph, visited, emails)
            if emails:
                info = [a[0]] + sorted(emails)
                res.append(info)
        
        return res



        ## S2: Union-Find
        ## T: O(NK⋅logNK+NK⋅α(N)) ~ O(NKlogNK), N = len(accounts) and K is the max length of an account
        ## S: O(NK)

        # find root
        def find(i):
            while root[i] != i:
                root[i] = root[root[i]]     # path compression
                i = root[i]
            return i
        
        # union find
        d = {}  # key:val = email:index
        root = list(range(len(accounts)))   
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in d:
                    r1, r2 = find(i), find(d[email])
                    root[r2] = r1
                else:
                    d[email] = i

        # merge accounts      
        acc = defaultdict(set)     # key:val = index: {set of emails}
        for i in range(len(accounts)):
            acc[find(i)] |= set(accounts[i][1:])
        
        # convert into required format
        res = []
        for k, v in acc.items():    
            res.append([accounts[k][0]] + sorted(v))
        
        return res