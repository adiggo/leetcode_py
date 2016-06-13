class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Since the requirements are unique digits which means the max value of n is 10. 
        # If n > 10, then return the res as 10
        if n <= 0:
            return 0 if n != 0 else 1
        # the fast solution should be related to how to know the duplicate digits number
        # pattern searching
        # for n == 1, there is 1 * 10 elements
        # for n == 2, there is 10 + (9 * 9) elements
        # for n == 3, there is 91 + (9 * 9 * 8) elements

        res = 10
        for i in xrange(2, n + 1):
            if i > 10:
                break
            tmp = 9
            poosible = 9
            for j in xrange(i-1):
                tmp *= poosible
                poosible -= 1
            res += tmp
        return res
