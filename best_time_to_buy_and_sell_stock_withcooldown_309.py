# reference: http://bookshadow.com/weblog/2015/11/24/leetcode-best-time-to-buy-and-sell-stock-with-cooldown/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # first element is the profits, second is index
        if not prices or len(prices) == 1:
            return 0
        l = len(prices)
        sell = [None] * l
        buy = [None] * l
        buy[0] = -prices[0]
        sell[0] = 0
        buy[1] = max(buy[0], -prices[1])
        sell[1] = max(0, prices[1]-prices[0])
        for i in xrange(2, l):
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
        
        return sell[-1]

