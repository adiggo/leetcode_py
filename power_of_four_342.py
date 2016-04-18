class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        while num > 1:
            if num % 4 == 0:
                num = num/4
            else:
                return False
        return True

class Solution2(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return not (num & (num-1)) and num > 0 and num & 0x55555555 == num
