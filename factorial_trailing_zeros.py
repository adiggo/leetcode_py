class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # only happens when 5 * even number or 0 * any
        res = 0
        while n/5 > 0:
            res += n/5
            n = n/5
        return res

