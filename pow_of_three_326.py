class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # since math.log(,3) will give you a double value which sort of like 4.9999999, so we need to round it and check whethere it equal to n
        return n > 0 and (3 ** round(math.log(n,3))) == n
