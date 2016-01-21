

#actually it was resolve via two dimensional array
#now it use 1-d. so we need to from k to 1
# local[i][j] means it need to has a transaction in ith day
# glocal[i][j] is the result we need
# local[i-1][j] + diff --> actually it is only one transaction, since it combine two transactiont together
# local[i][j] = max(global[i-1][j-1] + max(diff, 0), local[i-1][j]+diff)
# global[i][j] = max(global[i-1][j], local[i][j]) --> glocal ith day profit must be larger than i-1 th day. If ith is larger than i-1th, then we choose local[i][j] since it include ith day into transaction. else we use the i-1 th day profit. 
class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
        size = len(prices)
        if k > size / 2:
            return self.get_max_profit(size, prices)
        l = [0] * (k + 1)
        g = [0] *(k + 1)
        for i in range(1, size):
            diff = prices[i] - prices[i-1]
            for j in range(k , 0 , -1):
                # if j is even, then we sell stock, if it is odd, then we buy stock
                l[j] = max(l[j] + diff, g[j-1])
                g[j] = max(g[j], l[j])
        return g[k]

    # get max profit with unlimited transactions
    def get_max_profit(self, size, prices):
        sum = 0
        for x in range(size - 1):
            if prices[x + 1] > prices[x]:
                sum += prices[x + 1] - prices[x]
        return sum

