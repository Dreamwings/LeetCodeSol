class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        for i in range(1, len(w)):
            w[i] += w[i-1]
        
        self.w = w[:]
        self.n = len(w)

    def pickIndex(self):
        """
        :rtype: int
        """
        from random import randint
        from bisect import bisect_left
        
        
        ## Solution 1:
        x = randint(1, self.w[-1])
        return bisect_left(self.w, x)
    
        """
        ## Solution 2:
        x = randint(1, self.w[-1])
        lo, hi = 0, self.n - 1
        
        while lo < hi:
            m = (lo + hi) >> 1
            if x <= self.w[m]:
                hi = m
            else:
                lo = m + 1
        return lo
        """

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()