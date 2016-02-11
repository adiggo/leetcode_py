class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [-1] * amount
        for a in range(amount):
            if dp[a] < 0:
                continue
            for c in coins:
                if a+c > amount:
                    continue
                if dp[a+c] < 0 or dp[a+c] > dp[a]+1:
                    dp[a+c] = dp[a]+1
        return dp[amount]
