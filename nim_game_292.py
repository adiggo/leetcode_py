class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # base condition: n <= 3 A win, n == 4 B win, n == 5--7 A win, n == 8 B win, n == 9--11 A win
        if n % 4 == 0:
            return False
        else:
            return True
