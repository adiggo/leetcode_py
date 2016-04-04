class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # hindex <= len(citations)
        citations.sort()
        n = len(citations)
        for i in xrange(n):
            num = citations[i]
            if n - i <= num:
                return n - i
        return 0



class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # hindex <= len(citations)
        
        n = len(citations)
        dp = [0] * (n+1)
        for c in citations:
            if c > n:
                dp[n] = dp[n] + 1
            else:
                dp[c] = dp[c] + 1
        amount = 0
        for i in xrange(n, -1, -1):
            amount += dp[i]
            if amount >= i:
                return i
        return 0
            
