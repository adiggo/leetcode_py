class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in s:
            d = ord(c) - ord('A') + 1
            res = 26 * res + d
        return res
