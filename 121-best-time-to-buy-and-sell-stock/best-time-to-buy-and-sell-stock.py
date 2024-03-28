class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        m, res = prices[0], 0
        
        for x in prices:
            # better than prices[1:] because list slice takes time O(k)
            m = min(m, x)
            res = max(res, x - m)
        
        return res