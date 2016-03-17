class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        l1, l2 = len(s), len(p)
        if l2 - p.count('*') > l1:   #avoid TLE
            return False
        dp = [[0 for x in range(l1+1)] for x in range(l2+1)]
        dp[0][0] = 1
        for i in range(1, l2+1):
            dp[i][0] = 0 if p[i-1] != '*' else dp[i-1][0]
        for j in range(1, l1+1):
            dp[0][j] = 0
        for i in range(1, l2+1):
            for j in range(1, l1+1):
                if p[i-1] == s[j-1] or p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[i-1] == '*' and (dp[i-1][j] or dp[i][j-1]):
                        dp[i][j] = 1
        return True if dp[l2][l1] else False
