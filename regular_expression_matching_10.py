
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        l1, l2 = len(s), len(p)
        for i in range(min(l1, l2)):
            if s[i] == p[i]:
                continue
            else:
                # single character match
                if p[i] == '.':
                    continue
                elif p[i] == '*':
                    for j in range(l1-i):
                        if self.isMatch(p[i+1:], s[i+j:]):
                            return True
                        else:
                            continue
                else:
                    continue
        return True if l1 == l2 else False
       


# 
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp=[[False for i in range(n+1)] for j in range(m+1)]
        dp[0][0] = True
        for i in xrange(1, n+1):
            if i > 1 and p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
        
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if p[j-1] != '*' and p[j-1] != '.':
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
                elif p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == '.' ))
        return dp[m][n]
                    
                
