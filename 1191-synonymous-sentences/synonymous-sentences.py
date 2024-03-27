class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:

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