class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) < 2:
            return 0
        max_profit = 0
        # the idea is to find the max_profit with the constraint at most two transaction
        # use two array to record the max_value at each index from start to end, from end to start
        min_p = prices[0]
        max_p = prices[len(prices) - 1]
        max_profit1, max_profit2 = 0, 0
        max_p1 = []
        max_p2 = []
        for i in range(len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
            max_profit1 = max(max_profit1, prices[i] - min_p)
            max_p1.append(max_profit1)
            if prices[len(prices) - i - 1] > max_p:
                max_p = prices[len(prices)-i - 1]
            max_profit2 = max(max_profit2, max_p - prices[len(prices)-i - 1])
            max_p2.append(max_profit2)
        res = max_profit1
        for i in range(len(max_p1)):
            res = max(max_p1[i] + max_p2[len(max_p1) -1 -i], res)
        return res
