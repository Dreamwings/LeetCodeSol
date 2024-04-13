class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        ## S2: One Line
        ## T: O(N * K)
        ## S: O(1)

        return not any([val % len(words) for val in Counter("".join(words)).values()])

        """

        ## S1: Counter
        ## T: O(N * K)
        ## S: O(1)
        
        from collections import Counter

        d = Counter(''.join(words)) # d has at most 26 key value pairs
        n = len(words)

        for k, v in d.items():
            if v % n:
                return False

        return True

        """
