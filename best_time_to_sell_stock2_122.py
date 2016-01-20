class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """ 
        #   2 1 4 5 3 5
        #     1   5 3 5
        if prices is None or len(prices) < 2:
            return 0
        max_profit = 0
        for i in range(0: len(prices)-1):
            cur_price = prices[i]
            next_price = prices[i+1]
            if cur_price <= next_price:
                max_profit += next_price - cur_price
        return max_profit
