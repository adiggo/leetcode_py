class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # since math.log(,3) will give you a double value which sort of like 4.9999999, so we need to round it and check whethere it equal to n
        return n > 0 and (3 ** round(math.log(n,3))) == n


    def isPowerOfThree_recursion(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n <= 0 or n % 3 != 0:
            return False
        else:
            return self.isPowerOfThree(n/3)
