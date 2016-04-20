class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        #special case
        if n == 3 or n == 2:
            return n-1
        dp = [0] * (n+1)
        dp[2] = 2
        dp[3] = 3
        count = 1
        for i in xrange(4, n+1):
            if i == 4:
                dp[i] = i
            else:
                if count % 3 > 0:
                    dp[i] = (dp[i-1] / 2) * 3
                else:
                    dp[i] = (dp[i-1] / 3) * 4
                count += 1
        return dp[-1]
