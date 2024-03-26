class Solution:
    def alienOrder(self, words: List[str]) -> str:

        ## S1: Topological Sort with Heapq
        ## T: O(N * L)
        ## S: O(1)

        from collections import defaultdict, deque
        from heapq import heapify, heappush, heappop

        all_char = set("".join(words))
        graph = defaultdict(list)
        indeg = {c: 0 for c in all_char}

        # build the graph and get in degree values for each char
        for w1, w2 in zip(words[:-1], words[1:]):
            # consider a special case: "abc" before "ab"
            if len(w1) > len(w2) and w1[: len(w2)] == w2:
                return ""
            # for normal case, compare char from w1 and w2 one by one
            for x, y in zip(w1, w2):
                if x != y:
                    graph[x].append(y)  # all char after x: x -> y
                    indeg[y] += 1
                    break  # the first (x!=y) determines the order

        # use heapq for the case there are multiple valid order,
        # need to be in normal alphabeta order
        hq = []
        # first find those char with 0 in degree, which should be in front
        for k, v in indeg.items():
            if v == 0:
                hq.append(k)

        if not hq:
            return "" # no nodes to start, there is a cycle
        heapify(hq) # sort the order for char with 0 in degree
        res = ""

        while hq:
            x = heappop(hq)
            res += x
            for y in graph[x]:
                indeg[y] -= 1
                if indeg[y] == 0:
                    heappush(hq, y)

        if len(res) != len(all_char):
            return ""
        return res
        


