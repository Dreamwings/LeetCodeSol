class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        
        ## S2: DFS
        ## T: 
        ## S:

        graph = collections.defaultdict(list)
        for k,v in synonyms:
            graph[k].append(v)
            graph[v].append(k)
            
        res = set()
        stack = [text]
        while stack:
            cur_t = stack.pop()
            res.add(cur_t)
            
            cur_ws = cur_t.split()
            for i in range(len(cur_ws)):
                if cur_ws[i] in graph:
                    for rw in graph[cur_ws[i]]:
                        new_t = " ".join(cur_ws[:i] + [rw] + cur_ws[i+1:])
                        if new_t not in res:
                            stack.append(new_t)
                        
        return sorted(list(res))

        """

        ## S1: Iterative BFS
        ## T: 
        ## S:

        graph = collections.defaultdict(set)
        bfs = collections.deque()
        ans = set()
        bfs.append(text)
        for k,v in synonyms:
            graph[k].add(v)
            graph[v].add(k)
        while bfs:
            curT = bfs.popleft()
            ans.add(curT)
            words = curT.split()
            for i,w in enumerate(words):
                if w in graph.keys():
                    for newW in graph[w]:
                        newsent=' '.join(words[:i] + [newW] + words[i+1:])
                        if newsent not in ans:
                            bfs.append(newsent)
        return sorted(list(ans))

        ## S3: Union Find + DFS
        ## https://algo.monster/liteproblems/1258

        """