class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # the worst case is len(s)-1 cut
        # if the string is palindrome already, then 0 cut
        # the same idea: if the substring is palindrome, then zero cut
        if not s:
            return 0
        l = len(s)
        dp = [sys.maxint] * (l+1)
        dp[0] = -1
        is_palindrome = [[False] * l for x in xrange(l)]
        # should start from end
        for i in xrange(l-1, -1, -1):
            for j in xrange(i, l):
                if (i +1 > j-1 or is_palindrome[i+1][j-1]) and s[i] == s[j]:
                    is_palindrome[i][j] = True
        for i in xrange(1, l+1):
            for j in xrange(i-1, -1, -1):
                if is_palindrome[j][i-1]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[l]

        
