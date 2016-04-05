class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        lenS, lenT = len(s), len(t)
        dp = [0 for i in xrange(lenT + 1)]
        dp[0] = 1
        for i in xrange(lenS):
            for j in xrange(lenT, 0, -1):
                if s[i] == t[j - 1]:
                    dp[j] = dp[j] + dp[j - 1]
        return dp[lenT]



class Solution2(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0 for x in xrange(len(s) + 1)] for x in xrange(len(t) + 1)]
        for i in xrange(len(s)):
            dp[0][i] = 1
        for i in xrange(1, len(t)):
            dp[i][0] = 0
        for i in xrange(1, len(t)+1):
            for j in xrange(1, len(s)+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[len(t)][len(s)]
