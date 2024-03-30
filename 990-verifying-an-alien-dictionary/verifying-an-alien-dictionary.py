class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        ## S2:
        ## T: O(N)
        ## S: O(1)

        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1):

            for j in range(len(words[i])):
                # If we do not find a mismatch letter between words[i] and words[i + 1],
                # we need to examine the case when words are like ("apple", "app").
                if j >= len(words[i + 1]): return False

                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]: return False
                    # if we find the first different character and they are sorted,
                    # then there's no need to check remaining letters
                    break

        return True

        """
        ## S1:

        d = {c: i for i, c in enumerate(order)}
        
        def comp(x, y):
            i = 0
            while i < len(x) and i < len(y):
                if d[x[i]] < d[y[i]]:
                    return True
                elif d[x[i]] > d[y[i]]:
                    return False
                else:
                    i += 1
            if not x[i:]: return True
            return False
        
        for a, b in zip(words[:-1], words[1:]):
            if not comp(a, b):
                return False
            
        return True    
        """
        