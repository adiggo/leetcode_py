class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False] * (len(s) +1)
        dp[0] = True
        for i in xrange(len(s)):
            for j in xrange(i, -1, -1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1] = True
                    break
        return dp[len(s)]

