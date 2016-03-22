class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        # record n which is exponent
        exp = 2
        for i in range(num+1):
            if i == 0 or i == 1:
                res.append(i)
            else:
                exp = exp if i >= exp and i <  2 * exp else 2* exp
                index = i - exp
                res.append(res[index] + 1)
        return res
