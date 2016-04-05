class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
            r = (n-1) % 26
            res = chr(ord('A') + r) + res
            n = (n-1) / 26
        return res
