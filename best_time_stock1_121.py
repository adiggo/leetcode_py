class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) < 2:
            return 0
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            
            max_profit = max(max_profit, price-min_price)
        
        return max_profit
