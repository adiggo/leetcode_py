class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        while len(dp) <= n:
            m, squares = len(dp), n
            i = 1
            while i * i <= m :
                if dp[m-i*i] +1 < squares:
                    squares = dp[m-i*i] +1
                i += 1
            dp.append(squares)
        return dp[n]
