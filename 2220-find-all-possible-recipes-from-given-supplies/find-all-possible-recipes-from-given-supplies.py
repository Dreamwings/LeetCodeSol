class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        from collections import defaultdict, deque

        ## S1: Topological Sort
        ## T: O(N + M + V)
        ## S: O(N + M + V)

        graph = defaultdict(list)
        indeg = defaultdict(int)

        for rec, ings in zip(recipes, ingredients):
            for ing in ings:
                graph[ing].append(rec)
            indeg[rec] += len(ings)
        
        q = deque(supplies)
        res = []
        while q:
            for _ in range(len(q)):
                ing = q.popleft()
                for rec in graph[ing]:
                    indeg[rec] -= 1
                    if indeg[rec] == 0:
                        res.append(rec)
                        q.append(rec)
        return res