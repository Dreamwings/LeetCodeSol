class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        from collections import Counter

        ## Solution 2:
        ## T: O(N)
        ## S: O(1)

        res = cur = count_b = a = b = 0
        for c in tree:
            if c in (a, b):
                cur = cur + 1 
            else:
                cur = count_b + 1
            if c == b:
                count_b = count_b + 1 
            else:
                count_b = 1
            if b != c: 
                a, b = b, c
            res = max(res, cur)
        return res


        """
        ## S1: Sliding Window
        ## T: O(N)
        ## S: O(N)        
        
        d = Counter()
        res, i = 0, 0
        
        for j, v in enumerate(tree):
            d[v] += 1
            while len(d) > 2:
                d[tree[i]] -= 1
                if d[tree[i]] == 0:
                    del d[tree[i]]
                i += 1
            res = max(res, j - i + 1)
            
        return res
        """
        
