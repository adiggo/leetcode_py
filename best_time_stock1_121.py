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


#second round
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        res = 0
        local_min_price = sys.maxint
        for p in prices:
            if p < local_min_price:
                local_min_price = p
            else:
                res = max(p - local_min_price, res)
        return res
