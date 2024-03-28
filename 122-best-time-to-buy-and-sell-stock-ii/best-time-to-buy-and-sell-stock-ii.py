class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ## S1: Greedy
        
        n = len(prices)
        if n == 1: return 0
        
        profit = 0
        
        for a, b in zip(prices[:-1], prices[1:]):
            if a < b:
                profit += b - a
            
        return profit

        """
        ## S2: DP

        total_profit = 0
      
        # Loop through each pair of successive prices using pairwise()
        for buy_price, sell_price in pairwise(prices):
            # Calculate profit for the current pair
            # If sell price is greater than buy price, add the difference to total profit
            # Otherwise, add zero (no loss, no gain)
            profit = max(0, sell_price - buy_price)
            total_profit += profit
      
        # Return the total calculated profit
        return total_profit

        """