class Solution(object):
    def strStr(self, t, p):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # find next array
        # use next array to sort the 
        next = self.partial_match_table(p)
        i, j = 0, 0
        tL = len(t)
        pL = len(p)
        while i < tL and j < pL:
            if j == -1 or t[i] == p[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == pL:
            return i - j
        else:
            return -1
                
    def partial_match_table(self, pattern):
        """Compute the "next" table corresponding to pattern, for use in the
        Knuth-Morris-Pratt string search algorithm.
    
        """
        m = len(pattern)
        next = [-1] * m
        # pattern[k] is prefix, pattern[j] is suffix
        k = -1
        j = 0
        # abac
        while j < m - 1:
            if k == -1 or pattern[j] == pattern[k]:
                # 1. k = 0, j = 1, next[1] = 0
                # 3. k = 0, j = 2, next[2] = 0
                k += 1
                j += 1
                next[j] = k
            else:
                # 2. k = -1
                k = next[k]
        return next


