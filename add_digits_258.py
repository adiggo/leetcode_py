class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return (num-1) % 9 + 1 if num >= 1 else 0
